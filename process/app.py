from flask import Flask, jsonify, json, request, render_template
from pathlib import Path
from os.path import join
import yfinance as yf
import pandas as pd
import torch
import numpy as np
import joblib
import os
from datetime import timedelta
from utils.carregar_modelo import carregar_modelo_completo

# Caminhos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "modelo_lstm.pt")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")
scaler_y_path = os.path.join(BASE_DIR, "scaler_y.pkl")
dados_path = os.path.join(BASE_DIR, "..", "data", "dados_prever.csv")

# Carrega modelo e scalers
model, scaler, scaler_y = carregar_modelo_completo(model_path, scaler_path, scaler_y_path)
sequence_length = 20

# Inicializa o app Flask
app = Flask(__name__)

@app.route('/sobre', methods=['GET'])
def about():
    return '<h1>Pagina da rota Sobre</h1>'

# Puxando dados de yfinance e serializando
@app.route("/api/data", methods=['GET'])
def predict():
    try:
        symbol = request.args.get('symbol')
        start_date = request.args.get('dtstart')
        end_date = request.args.get('dtend')

        df = yf.download(symbol, start=start_date, end=end_date)

        # Garante que as colunas não sejam MultiIndex
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [' '.join(col).strip() for col in df.columns]

        df = df.reset_index()
        df['Ticker'] = symbol
        df.columns = [col.replace(f" {symbol}", "") if isinstance(col, str) else col for col in df.columns]


        # Converte para lista de dicionários (JSON serializável)
        return jsonify(df.to_dict(orient="records"))


    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Função de previsão multi-step
def multi_step_forecast(model, last_sequence, steps_ahead):
    """
    Gera previsão direta de até 60 dias com base na última sequência.
    """
    model.eval()
    steps_ahead = min(max(1, steps_ahead), 60)  # garante entre 1 e 60

    with torch.no_grad():
        out = model(last_sequence.unsqueeze(0))  # shape: (1, 60)
        preds = out.squeeze().cpu().numpy().tolist()

    return preds[:steps_ahead]

# Rota principal que serve o HTML
@app.route("/", methods=["GET"])
def home():
    return render_template("upload.html")

# Rota de previsão futura
@app.route("/prever_futuro", methods=["GET"])
def prever_futuro():
    try:
        df = pd.read_csv(dados_path)
        colunas_usadas = scaler.feature_names_in_
        df_filtrado = df[colunas_usadas].tail(sequence_length)

        if len(df_filtrado) < sequence_length:
            return jsonify({"erro": f"Arquivo precisa de pelo menos {sequence_length} linhas."}), 400

        dados_norm = scaler.transform(df_filtrado)
        entrada = torch.tensor(dados_norm, dtype=torch.float32)

        # Lê o parâmetro da URL, com valor padrão 30 e limite de 60
        steps_ahead = int(request.args.get("dias", 30))
        steps_ahead = min(max(1, steps_ahead), 60)

        preds = multi_step_forecast(model, entrada, steps_ahead)

        multi_preds_descaled = scaler_y.inverse_transform(np.array(preds).reshape(-1, 1)).flatten().tolist()

        ultima_data = pd.to_datetime(df["Timestamp"].max(), unit="s")
        future_dates = pd.date_range(start=ultima_data + timedelta(days=1), periods=steps_ahead, freq="D")
        future_dates = future_dates.strftime("%Y-%m-%d").tolist()

        return jsonify({
            "datas": future_dates,
            "previsoes": [round(v, 2) for v in multi_preds_descaled]
        })

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Executa o servidor
if __name__ == "__main__":
    app.run(debug=True)