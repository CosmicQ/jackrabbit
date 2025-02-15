from pymongo import MongoClient
from flask import Flask, jsonify

app = Flask(__name__)

# Connect to MongoDB (use the service name from your Kubernetes setup)
client = MongoClient("mongodb://mongo:27017/")  # 'mongo' is the service name
db = client['ride_share']

@app.route('/ping')
def ping():
    # Test the connection
    try:
        db.command("ping")
        return jsonify({"status": "MongoDB connected"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

