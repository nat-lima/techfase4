# Usa uma imagem base com Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos da pasta process/ para o container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "app.py"]