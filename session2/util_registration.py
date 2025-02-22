#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    with open("users.json", "a") as file:
        json.dump({"username": username, "password": password}, file)
        file.write("\n")

    return jsonify({"message": "Utilisateur enregistré avec succès!"})

if __name__ == '__main__':
    app.run(debug=True)
