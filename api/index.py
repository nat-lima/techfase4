from flask import Flask, jsonify, json, request
from pathlib import Path
from os.path import join
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1>Página da rota Home</h1>'

@app.route('/sobre', methods=['GET'])
def about():
    return '<h1>Pagina da rota Sobre</h1>'

# Puxando dados de yfinance e serializando
@app.route("/api/predict", methods=['GET'])
def predict():
    symbol = request.args.get('symbol')
    start_date = request.args.get('dtstart')
    end_date = request.args.get('dtend')

    # Use a função download para obter os dados
    df = yf.download(symbol, start=start_date, end=end_date)
    json_str = df.to_json(orient="records")
    return jsonify(json_str)

if __name__ == '__main__':
    app.run()