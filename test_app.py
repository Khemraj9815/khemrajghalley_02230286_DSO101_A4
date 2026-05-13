"""
Unit Tests for Flask Application
Tests all endpoints and functionality using pytest
"""

import pytest
import json
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHomeEndpoint:
    """Tests for the home endpoint"""
    
    def test_home_status_code(self, client):
        """Test that home endpoint returns 200 status code"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_home_response_format(self, client):
        """Test that home endpoint returns valid JSON"""
        response = client.get('/')
        data = json.loads(response.data)
        assert 'message' in data
        assert 'status' in data
        assert data['status'] == 'success'
    
    def test_home_message(self, client):
        """Test that home endpoint returns correct message"""
        response = client.get('/')
        data = json.loads(response.data)
        assert 'CI/CD Pipeline Demo App' in data['message']


class TestHelloEndpoint:
    """Tests for the hello endpoint"""
    
    def test_hello_default(self, client):
        """Test hello endpoint with default parameter"""
        response = client.get('/api/hello')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['message'] == 'Hello, World!'
    
    def test_hello_with_name(self, client):
        """Test hello endpoint with custom name"""
        response = client.get('/api/hello?name=Alice')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['message'] == 'Hello, Alice!'
    
    def test_hello_response_status(self, client):
        """Test that hello endpoint returns success status"""
        response = client.get('/api/hello')
        data = json.loads(response.data)
        assert data['status'] == 'success'


class TestHealthCheckEndpoint:
    """Tests for the health check endpoint"""
    
    def test_health_check_status(self, client):
        """Test health check endpoint"""
        response = client.get('/api/health')
        assert response.status_code == 200
    
    def test_health_check_healthy(self, client):
        """Test that health check returns healthy status"""
        response = client.get('/api/health')
        data = json.loads(response.data)
        assert data['status'] == 'healthy'


class TestDataEndpoint:
    """Tests for the data endpoint"""
    
    def test_get_data_status(self, client):
        """Test data endpoint returns 200"""
        response = client.get('/api/data')
        assert response.status_code == 200
    
    def test_get_data_structure(self, client):
        """Test data endpoint returns correct structure"""
        response = client.get('/api/data')
        data = json.loads(response.data)
        assert 'items' in data
        assert 'total' in data
        assert len(data['items']) == 3
    
    def test_get_data_items(self, client):
        """Test data items have correct structure"""
        response = client.get('/api/data')
        data = json.loads(response.data)
        for item in data['items']:
            assert 'id' in item
            assert 'name' in item
            assert 'value' in item


class TestAddEndpoint:
    """Tests for the add numbers endpoint"""
    
    def test_add_numbers_valid(self, client):
        """Test adding two numbers"""
        response = client.post('/api/add', 
                             json={'num1': 5, 'num2': 3})
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == 8
    
    def test_add_numbers_negative(self, client):
        """Test adding negative numbers"""
        response = client.post('/api/add',
                             json={'num1': -5, 'num2': 3})
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == -2
    
    def test_add_numbers_zeros(self, client):
        """Test adding zeros"""
        response = client.post('/api/add',
                             json={'num1': 0, 'num2': 0})
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['result'] == 0
    
    def test_add_numbers_status(self, client):
        """Test add endpoint returns success status"""
        response = client.post('/api/add',
                             json={'num1': 10, 'num2': 20})
        data = json.loads(response.data)
        assert data['status'] == 'success'


class TestErrorHandling:
    """Tests for error handling"""
    
    def test_404_not_found(self, client):
        """Test that non-existent endpoint returns 404"""
        response = client.get('/api/nonexistent')
        assert response.status_code == 404
    
    def test_404_response_format(self, client):
        """Test 404 response format"""
        response = client.get('/api/nonexistent')
        data = json.loads(response.data)
        assert data['status'] == 'error'
        assert 'error' in data


class TestMathOperations:
    """Tests for mathematical operations"""
    
    def test_simple_math(self):
        """Test basic math operations"""
        assert 1 + 1 == 2
        assert 5 - 3 == 2
        assert 3 * 4 == 12
        assert 10 / 2 == 5
    
    def test_addition(self):
        """Test addition"""
        result = 100 + 200
        assert result == 300
    
    def test_multiplication(self):
        """Test multiplication"""
        result = 15 * 4
        assert result == 60
