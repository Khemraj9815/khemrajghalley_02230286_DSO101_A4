from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# home endpoint
@app.route('/', methods=['GET'])
def home():
    """Home endpoint - returns a welcome message"""
    return jsonify({
        'message': 'Welcome to CI/CD Pipeline Demo App',
        'status': 'success',
        'timestamp': datetime.now().isoformat()
    }), 200

# error handling for 404 and 500 errors
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Not Found',
        'status': 'error'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal Server Error',
        'status': 'error'
    }), 500


if __name__ == '__main__':
    # For production, this should be run with a proper WSGI server
    app.run(host='0.0.0.0', port=5000, debug=False)
