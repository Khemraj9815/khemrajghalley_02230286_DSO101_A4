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
        assert 'This is CI/CD Pipeline demo app' in data['message']

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
