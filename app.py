from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection
# Adjust according to your mongo URI
MONGO_URI = ""
client = MongoClient(MONGO_URI)
db = client["SIC_UNI091"]  # Change to your database name
collection = db["sensor_data"]  # Collection for sensor data

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Received Data: {data}")

    # Store in MongoDB
    collection.insert_one(data)

    return jsonify({"status": "success"}), 200

@app.route('/status', methods=['GET'])
def status():
    try:
        # Attempt to ping the MongoDB server
        client.admin.command('ping')
        return jsonify({"status": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)