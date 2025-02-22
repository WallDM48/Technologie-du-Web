from flask import Flask, request, jsonify
#from flask_cors import CORS  # Добавяне на CORS

app = Flask(__name__)
#CORS(app)  # Активираме CORS

@app.route('/perform-addition', methods=['POST'])
def perform_addition():
    try:
        # Получаваме JSON данни
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        
        # Изчисляваме сумата
        result = num1 + num2
        
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
