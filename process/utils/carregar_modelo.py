import torch
import torch.nn as nn
import joblib
from utils.lstm_ativacao import LSTMAtivacao

# Função para carregar modelo e scalers
def carregar_modelo_completo(caminho_modelo):
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

    print("Modelo carregado com sucesso.")
    return model, checkpoint
