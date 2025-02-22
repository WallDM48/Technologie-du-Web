#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app) 

@app.route('/square-root', methods=['POST'])
def square_root():
    data = request.json
    number = float(data.get('number', 0))
    result = math.sqrt(number)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
