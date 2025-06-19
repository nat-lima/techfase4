class Config:
    SECRET_KEY = 'your_secret_key'
    CACHE_TYPE = 'simple'
    SWAGGER = {
        'title': 'Dados Abertos PRF',
        'uiversion': 3,
        "paths": {
                    "/scrape/dadosabertosprf": {
                    "get": {
                        "tags": [
                        "Produção"
                        ],
                        "summary": "Retrieve data from 2025 e 2024 from https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes (Producao). ",
                        "responses": {
                        "200": {
                            "description": "Successfull",
                            "content": {
                            "application/json": {
                                "schema": {
                                "$ref": "#/scrape/"
                                }
                            }
                            }
                        }
                        }
                        }
                    },
                    "/auth/login": {
                    "post": {
                        "tags": [
                        "Login"
                        ],
    "requestBody": { "required": True, "content": { "application/json": { "schema": { "$ref": "#/components/schemas/LoginRequest" } } } } ,        
    "summary": "HTTP Request for login",
                        "responses": {
                        "200": {
                            "description": "Successful",
                            "content": {
                            "application/json": {
                                "schema": {
                                "$ref": "#/auth/"
                                }
                            }
                            }
                        }
                        }
                        }
                    }
            }
    }