from flask import Flask, request, jsonify, render_template
import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import joblib
import os
from utils.lstm_ativacao import LSTMAtivacao
from utils.carregar_modelo import carregar_modelo_completo

# Caminhos absolutos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "modelo_lstm.pt")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")
scaler_y_path = os.path.join(BASE_DIR, "scaler_y.pkl")

# Carrega modelo e scalers
model, scaler, scaler_y = carregar_modelo_completo(model_path, scaler_path, scaler_y_path)
sequence_length = 20
print("Colunas esperadas pelo scaler:", scaler.feature_names_in_)

# Inicialização do Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("upload.html")

@app.route("/prever_csv", methods=["POST"])
def prever_csv():
    if "arquivo" not in request.files:
        return jsonify({"erro": "Nenhum arquivo enviado com a chave 'arquivo'."}), 400

    arquivo = request.files["arquivo"]

    try:
        df = pd.read_csv(arquivo)
        colunas_usadas = scaler.feature_names_in_
        df_filtrado = df[colunas_usadas].tail(sequence_length)

        if len(df_filtrado) < sequence_length:
            return jsonify({"erro": f"O CSV precisa ter pelo menos {sequence_length} linhas válidas."}), 400

        dados_norm = scaler.transform(df_filtrado)
        entrada = torch.tensor([dados_norm], dtype=torch.float32)

        with torch.no_grad():
            saida = model(entrada).numpy().flatten()[0]
            pred_desscalada = scaler_y.inverse_transform([[saida]])[0][0]

        closes_desscalados = scaler_y.inverse_transform(dados_norm[:, -1].reshape(-1, 1)).flatten().tolist()

        return jsonify({
            "previsao_close": round(pred_desscalada, 2),
            "ultimos_closes": closes_desscalados
        })

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)