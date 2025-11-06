import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'DevOps Lab' in data['message']

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_info_endpoint(client):
    response = client.get('/info')
    assert response.status_code == 200
    data = response.get_json()
    assert 'hostname' in data
