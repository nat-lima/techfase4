from flask import Flask, jsonify, render_template
import torch
import numpy as np
import pandas as pd
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

# Função de previsão multi-step
def multi_step_forecast(model, last_sequence, steps_ahead):
    model.eval()
    preds = []
    seq = last_sequence.clone().detach()

    for _ in range(steps_ahead):
        with torch.no_grad():
            out = model(seq.unsqueeze(0))
            preds.append(out.item())

            new_step = seq[-1].clone()
            new_step[0] = out  # substitui o valor de 'Close'
            seq = torch.cat((seq[1:], new_step.unsqueeze(0)), dim=0)

    return preds

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

        steps_ahead = 30
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