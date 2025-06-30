import torch
import torch.nn as nn
import joblib
from utils.lstm_ativacao import LSTMAtivacao

# Função para carregar modelo e scalers
def carregar_modelo_completo(caminho_modelo, caminho_scaler, caminho_scaler_y):
    checkpoint = torch.load(caminho_modelo, map_location="cpu")

    ativacoes = {
        "ReLU": nn.ReLU(),
        "Tanh": nn.Tanh(),
        "Sem_Ativacao": nn.Identity()
    }

    model = LSTMAtivacao(
        input_size=checkpoint["input_size"],
        hidden_size=checkpoint["hidden_size"],
        num_layers=checkpoint["num_layers"],
        output_size=checkpoint["output_size"],
        ativacao=ativacoes[checkpoint["activation"]]
    )
    model.load_state_dict(checkpoint["model_state"])
    model.eval()

    scaler = joblib.load(caminho_scaler)
    scaler_y = joblib.load(caminho_scaler_y)

    print("Modelo e scalers carregados com sucesso.")
    return model, scaler, scaler_y