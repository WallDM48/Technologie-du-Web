#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/news', methods=['GET'])
def get_news():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()[:5]  # Взимаме само първите 5 публикации
        return jsonify(data)
    else:
        return jsonify({"error": "Échec de récupération des nouvelles"}), 500

if __name__ == '__main__':
    app.run(debug=True)
