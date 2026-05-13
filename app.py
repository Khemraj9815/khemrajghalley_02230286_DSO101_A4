"""
Flask Application for CI/CD Pipeline Demo
A simple backend API with multiple endpoints for testing and deployment
"""

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """Home endpoint - returns a welcome message"""
    return jsonify({
        'message': 'Welcome to CI/CD Pipeline Demo App',
        'status': 'success',
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/api/hello', methods=['GET'])
def hello():
    """Hello API endpoint - returns a greeting"""
    name = request.args.get('name', 'World')
    return jsonify({
        'message': f'Hello, {name}!',
        'status': 'success'
    }), 200


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint - returns app status"""
    return jsonify({
        'status': 'healthy',
        'app': 'CI/CD Pipeline Demo',
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/api/data', methods=['GET'])
def get_data():
    """API endpoint that returns sample data"""
    data = {
        'items': [
            {'id': 1, 'name': 'Item 1', 'value': 100},
            {'id': 2, 'name': 'Item 2', 'value': 200},
            {'id': 3, 'name': 'Item 3', 'value': 300}
        ],
        'total': 3
    }
    return jsonify(data), 200


@app.route('/api/add', methods=['POST'])
def add_numbers():
    """API endpoint that adds two numbers"""
    try:
        data = request.get_json()
        num1 = data.get('num1', 0)
        num2 = data.get('num2', 0)
        result = num1 + num2
        
        return jsonify({
            'num1': num1,
            'num2': num2,
            'result': result,
            'status': 'success'
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400


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
