
from flask import request, jsonify
from app import app, auth, config
from app.data.dadosabertosprf import get_content_dadosabertosprf

#ROUTE PRODUCAO
@app.route('/scrape/dadosabertosprf', methods=['GET'])
@auth.login_required
def scrape_dadosabertosprf():
    return get_content_dadosabertosprf()



 