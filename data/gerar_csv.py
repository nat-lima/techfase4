import pandas as pd
from datetime import datetime, timedelta
import os

# Caminho dinâmico para a pasta 'data'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
destino = os.path.join(BASE_DIR, "..", "data")
os.makedirs(destino, exist_ok=True)
caminho_csv = os.path.join(destino, "dados_prever.csv")

# Parâmetros iniciais
data_inicial = datetime(2024, 6, 10)
linhas = []

for i in range(20):
    data = data_inicial + timedelta(days=i)
    timestamp = int(data.timestamp())
    dia_da_semana = data.weekday()

    linhas.append({
        "Close": round(10 + i * 0.2, 2),
        "High": round(10 + i * 0.4, 2),
        "Low": round(10 + i * 0.1, 2),
        "Open": round(10 + i * 0.3, 2),
        "Volume": 120000 + i * 5000,
        "Timestamp": timestamp,
        "Year": data.year,
        "Month": data.month,
        "Day": data.day,
        "WeekDay": dia_da_semana,
        "Ticker": "ACN"
    })

df = pd.DataFrame(linhas)
df.to_csv(caminho_csv, index=False)

print(f"✅ Arquivo 'dados_prever.csv' salvo em:\n{os.path.abspath(caminho_csv)}")