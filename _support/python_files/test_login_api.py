 import requests

def test_login_api_success():
    url = "http://exemplo.com/api/login"
    payload = {
        "username": "admin",
        "password": "admin123"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert "token" in response.json()

