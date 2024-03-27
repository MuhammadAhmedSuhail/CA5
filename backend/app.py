from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://database:27017/")
db = client["mydatabase"]
collection = db["userdata"]

@app.route('/store', methods=['POST'])
def store_data():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    if name and email:
        collection.insert_one({'name': name, 'email': email})
        return jsonify({'message': 'Data stored successfully'}), 200
    else:
        return jsonify({'error': 'Name and email are required'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
