from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from DevOps Lab/Hello from DevOps Lab - CI-CD Pipeline v1.0',
        'version': os.getenv('VERSION', '1.0.0'),
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'hostname': socket.gethostname(),
        'pod_ip': os.getenv('POD_IP', 'unknown')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': __import__('datetime').datetime.now().isoformat()})

@app.route('/metrics')
def metrics():
    return jsonify({
        'requests_served': 1000,
        'memory_usage': '45%',
        'status': 'operational'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
