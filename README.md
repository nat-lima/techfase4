### Challenge Fiap 4 etapa:

- predizer o valor de fechamento da bolsa de valores de uma empresa 
- pipeline de desenvolvimento:
    - criação do modelo preditivo
    - deploy do modelo em uma API que permita a previsão de preços de ações


## Link video

https://drive.google.com/drive/folders/1Wy_kNKhRWtRm2lDKU4m8vf-SMGHgF2od?usp=sharing


## Arquitetura

## 📁 Estrutura do Projeto

```bash

TECHFASE4/
└── data/
    ├──dados.pkl
    ├──get_data.ipynb
└── process/
    ├── mlruns/
    ├── templates/
    │   └── upload.html
    ├── utils/
    │   └── __init__.py
    │   └── carregar_modelo.py
    │   └── lstm_ativacao.py
    ├── .dockerignore    
    ├── app.py
    ├── Dockerfile   
    ├── lstm sem scaler.ipynb
    ├── modelo_lstm.pt
    ├── requirements.txt
└── .gitignore
└── README.md

```

- **`data/`**: Diretório principal do aplicativo.
  - **`dados.pkl`**: Contém o data frame pickle para treinamento do Modelo.
  - **`get_data.ipynb`**: instanciada apartir de rota no app.py, ao reconhecer os paramentos ação, data inicio e data fim o script salva o resultado da consulta  como data frame pickle. 
- **`process/`**: 
  - **`mlruns/`**: Experimentos executados.
  - **`templates/`**: 
      - **`upload.html`**: Instanciado apartir de rota no app.py, o html template possui entrada para recebimento de parametro, bem como, estrutura para  e aprsentar o gráfico de previsões (invocada apartir do flask)
- **`util/`**:
   - **`carregar_modelo.py`**: Carrega o Modelo previamente treinado
   - **`lstm_ativacao.py`**: Desenvolvimento da LSTM para prever o preço de fechamento.
- **`app.py`**: Contém rota para busca dos dados financeiro utilizando o yfinannce, e contém rota para apresentação das previsões ao usuário final.
- **`lstm sem scaler.ipynb`**: Opcoes de ativações para análise de qual entre elas performa melhor.
- **`modelo_lstm.pt`**: Modelo treinado 
- **`requirements.txt`**: Lista de dependências do projeto.
- **`README.md`**: Documentação do projeto.


## Criar imagem no Docker

Abrir DOCKER DESKTOP

Construa a imagem: docker build -t flask-previsao .

pasta requirements.txt deve estar dentro da pasta onde esta o dockerfile.

Depois que o build terminar com sucesso: docker run -p 5000:5000 flask-previsao

API Flask estará disponível em:
http://localhost:5000


🧪 Verificar se a imagem foi criada
Para listar as imagens locais: docker images


🔁 Para reconstruir a imagem
Rodar docker build de novo se:
•	Alterou o Dockerfile
•	Atualizou o requirements.txt
•	Mudou arquivos do seu app (como app.py, modelos .pt, templates, etc.)
•	Adicionou novas dependências ou arquivos ao projeto

Nesses casos, reconstruir com: docker build -t flask-previsao . 
