### Challenge Fiap 4 etapa:

- predizer o valor de fechamento da bolsa de valores de uma empresa 
- pipeline de desenvolvimento:
    - criação do modelo preditivo
    - deploy do modelo em uma API que permita a previsão de preços de ações


Estrutura do projeto:

techfase4/
└── api/
    ├──index.py
└── data/
    ├──dados_prever.csv
    ├──dados.pkl
    ├──gerar_csv.py
    ├──get_data.ipynb
└── process/
    ├── mlruns/
    └── templates/
        └── upload.html
    ├── utils/
    │   ├── __init__.py
    │   └── carregar_modelo.py
    │   ├── lstm_ativacao.py
    ├── app.py
    ├── lstm_v2.ipynb
    ├── modelo_lstm.pt
    ├── scaler_y.pkl
    ├── scaler.pkl


