import pytest
from app import ACEestApp

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to ACEest Fitness & Gym!" in response.data