from flask import Flask, request, jsonify
import pandas as pd
import base64
from tinydb import TinyDB, Query
import datetime as dt

app = Flask(__name__)

db = TinyDB('db2.json')
dataset = pd.read_csv('dataset.csv')
if not dataset.empty:
    print("Dataset loaded successfully")
else:
    print("Failed to load dataset")

@app.route('/model', methods=['GET'])
def get_model():
    response = {}
    with open('../FederatedLearning/model2.tflite', 'rb') as f:
        response['model_encoded'] = base64.b64encode(f.read()).decode('ascii')
    print("model sent successfully")
    return jsonify(response)

# Rota para obter dados via solicitação GET
@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    data['time'] = dt.datetime.now().isoformat()
    db.insert(data)
    print(data)
    return jsonify({'message': 'data received successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)