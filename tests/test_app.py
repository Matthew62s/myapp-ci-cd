import pytest
import sys
import os

#Добавляем src в путь чтобы импортировать app
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    """Простой тест который всегда работает"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_hello_endpoint_exists(client):
    """Проверяем что главная страница отвечает"""
    response = client.get('/')
    assert response.status_code == 200
