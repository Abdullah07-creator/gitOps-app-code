import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables Cross-Origin requests from our Frontend

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "service": "backend"}), 200

@app.route('/api/info', methods=['GET'])
def info():
    app_version = os.getenv("APP_VERSION", "v1.0.0")
    return jsonify({
        "message": "Hello from GitOps Backend Microservice!",
        "version": app_version,
        "status": "online"
    }), 200

if __name__ == '__main__':
    # Binds to 0.0.0.0 so external/container requests are accepted
    app.run(host='0.0.0.0', port=5000)
