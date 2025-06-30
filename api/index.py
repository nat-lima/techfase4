from flask import Flask, jsonify, json, request
from pathlib import Path
from os.path import join
import yfinance as yf
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1>Página da rota Home</h1>'

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

if __name__ == '__main__':
    app.run()