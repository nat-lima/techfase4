<<<<<<< HEAD
# Embrapa

Este é um projeto de API desenvolvido com Flask, que inclui web scraping em páginas do dominio http://vitibrasil.cnpuv.embrapa.br/ e autenticação básica.

## Link video

https://drive.google.com/file/d/1kI1DZXqvbvSgiWLqt8x2JfOiQ-eMeRmE/view?usp=sharing

## 🚀 Funcionalidades

- **Autenticação Básica**: Protege rotas sensíveis usando autenticação HTTP básica.
- **Web Scraping**: Extrai dados de páginas web http://vitibrasil.cnpuv.embrapa.br/ (label, table, tbody, tr, td) usando BeautifulSoup.
- **API Embrapa**: Expõe dados provenientes da extração da pagina web vitibrasil em formato JSON.
- **Cache e Documentação**: Implementa cache para otimização e documentação automática com Swagger.

## 📁 Estrutura do Projeto

```bash
techfase1/
├── app/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── comercializacao.py
│   │   ├── exportacao.py
│   │   └── importacao.py
│   │   └── processamento.py
│   │   └── producao.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── scrape.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── auth.py
│   │   ├── linksviti.py
│   └── config.py
├── requirements.txt
├── README.md
└── run.py
```

- **`app/`**: Diretório principal do aplicativo.
  - **`data/`**: Classes para lógica de negócios para scrapping das informações (comercializacao, exportacao, importacao, processamento, produção) do site da embrapa.
  - **`routes/`**: Contém as rotas organizadas por acesso aos dados no site da embrapa. 
                   As rotas não recebem argumentos uma vez que o método captura todas as datas disponíveis no site para consulta.
  - **`utils/`**: Utilitários, como autenticação.
  - **`config.py`**: Configurações da aplicação Flask.
- **`run.py`**: Ponto de entrada para iniciar o aplicativo.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`Dockerfile`**: Configurações para Docker.
- **`README.md`**: Documentação do projeto.

## 🛠️ Como Executar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/nat-lima/techfase1
cd techfase1
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Aplicativo

```bash
python run.py
```

O aplicativo estará disponível em `http://localhost:5000` ou `http://127.0.0.1:5000`

Acesse a aplicação em `http://localhost:5000`.

### 5. Deploy na Vercel

Instale o Node.js.

Crie uma conta na Vercel em https://vercel.com/.

Instale no VSCode a extensão da Vercel oficial.

Criar arquivo vercel.json:
```bash
{
    "version": 2,
    "builds": [
      {
        "src": "run.py",
        "use": "@vercel/python"
      }
    ],
    "routes": [
      { "src": "/(.*)", "dest": "run.py" }
    ]
  }
```
Rode no terminal:

```bash
npm i -g vercel
vercel
vercel --prod
```

Link vercel: https://techfase1-angn7okrl-vivianas-projects-ee28f91d.vercel.app/

Link vercel doc api: https://techfase1-angn7okrl-vivianas-projects-ee28f91d.vercel.app/apidocs/

### 6. Arquitetura

![Arquitetura](https://github.com/user-attachments/assets/1c9cb1fc-33f2-4c07-8d13-ae595bf406e9)

## 📖 Documentação da API

A documentação da API é gerada automaticamente com Swagger e está disponível em `http://localhost:5000/apidocs/`.

## 🤝 Contribuindo

1. Fork este repositório.
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Faça push para sua branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.
instalar, configurar e usar o projeto. Ele também cobre contribuições, contato, licença e agradecimentos, tornando-o completo e fácil de entender para novos desenvolvedores.
=======
# Dados Abertos PRF

Este é um projeto de API desenvolvido com Flask, que inclui web scraping https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes e autenticação básica.

## Link video



## 🚀 Funcionalidades

- **Autenticação Básica**: Protege rotas sensíveis usando autenticação HTTP básica.
- **Web Scraping**: Extrai o csv de 2024 e 2025 sobre acidentes da página web https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes
- **Dados Abertos**: Expõe dados provenientes da extração do download de arquivos no formato csv.
- **Cache e Documentação**: Implementa cache para otimização e documentação automática com Swagger.

## 📁 Estrutura do Projeto

```bash
techfase1/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── scrape.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── auth.py
│   │   ├── links.py
│   └── config.py
├── requirements.txt
├── README.md
└── run.py
└── scrape_detratan.py
```

- **`app/`**: Diretório principal do aplicativo.
  - **`routes/`**: Contém as rotas organizadas por acesso aos dados no site de dados abertos da PRF. 
                   As rotas não recebem argumentos uma vez que o método captura todas as datas disponíveis no site para consulta.
  - **`utils/`**: Utilitários, como autenticação.
  - **`config.py`**: Configurações da aplicação Flask.
- **`run.py`**: Ponto de entrada para iniciar o aplicativo.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`README.md`**: Documentação do projeto.

## 🛠️ Como Executar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/nat-lima/techfase3
cd techfase3
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Aplicativo

```bash
python run.py
```

O aplicativo estará disponível em `http://localhost:5000` ou `http://127.0.0.1:5000`

Acesse a aplicação em `http://localhost:5000`.

### 5. Arquitetura




## 📖 Documentação da API

A documentação da API é gerada automaticamente com Swagger e está disponível em `http://localhost:5000/apidocs/`.

## 🤝 Contribuindo

1. Fork este repositório.
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Faça push para sua branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.
instalar, configurar e usar o projeto. Ele também cobre contribuições, contato, licença e agradecimentos, tornando-o completo e fácil de entender para novos desenvolvedores.
>>>>>>> 5d8c14d8b292a4a718c24f2f8749b4d5dc2161f8
