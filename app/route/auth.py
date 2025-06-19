from flask import jsonify
from app import app, auth

@app.route('/')
def home():
    return "Hello Anonimous user!"

@app.route('/auth/login', methods=['GET'])
@auth.login_required 
def login():
    username = format(auth.current_user())
    return jsonify({"message": "Hello: " + username })


