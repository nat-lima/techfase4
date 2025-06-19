import requests
import csv
import zipfile
import pandas as pd
import numpy as np
import time
from app.utils.links import url_dadosabertos_prf_2025,url_dadosabertos_prf_2024, url_dadosabertos_prf_2023
import firebase_admin # type: ignore
from firebase_admin import credentials # type: ignore
from firebase_admin import firestore # type: ignore
from flask import jsonify
import logging

def get_content_dadosabertosprf():
    try:
        logging.basicConfig(filename="app/logdadosabertosprf.log", filemode="w", format="%(name)s → %(levelname)s: %(message)s")

        response = requests.get(url_dadosabertos_prf_2025)
        with open("dados/datatran2025.zip", "wb") as file:
            file.write(response.content)
            logging.warning("Download concluído 2025!" + url_dadosabertos_prf_2025)

        # Caminho do arquivo ZIP e da pasta de destino
        zip_path = "dados/datatran2025.zip"
        extract_path = "dados/"

        response = requests.get(url_dadosabertos_prf_2024)
        with open("dados/datatran2024.zip", "wb") as file:
            file.write(response.content)
            logging.warning("Download concluído 2025!" + url_dadosabertos_prf_2024)

        # Caminho do arquivo ZIP e da pasta de destino
        zip_path = "dados/datatran2024.zip"
        extract_path = "dados/"

        # Abrir e extrair o ZIP
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)

        # Use a service account
        cred = credentials.Certificate('app/key/techfase3-firebase-adminsdk-fbsvc-e71cc04b8f.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        logging.warning("Conexão aberta!")

        count = 0
        doc_ref = db.collection("datatran")
        logging.warning("reading 2025!")        
        with open('dados/datatran2025.csv', newline='', encoding='latin-1') as csvfile:
            reader = csv.DictReader(csvfile,delimiter=';')
            for row in reader:
                count = count + 1
                doc_ref.add(row)
                break

        logging.warning("Finished reading 2025!")
        dict1 = {'File': 'datatran2025.csv', 'Lines Inserted': count}
                
        count = 0
        logging.warning("reading 2024!")   
        with open('dados/datatran2024.csv', newline='', encoding='latin-1') as csvfile:
            reader2 = csv.DictReader(csvfile,delimiter=';')
            for row2 in reader2:
                count = count + 1
                doc_ref.add(row2)
                break
        logging.warning("Finished reading 2025!")
        dict2 = {'File': 'datatran2024.csv', 'Lines Inserted': count}    
 
        logging.warning(jsonify(dict1,dict2)) 
        return jsonify(dict1,dict2)    
                              
    except Exception as e:
        return (jsonify(str(e))), 500
