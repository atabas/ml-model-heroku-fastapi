# Tests for the API
from starter.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_home():
    r = client.get('/')
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, Welcome to the Census Data model app!"}

def test_predict_less_than_50():
    data = {
        "age": 0,
        "workclass": "Private",
        "fnlwgt": 0,
        "education": "Bachelors",
        "education_num": 0,
        "marital_status": "Married-civ-spouse",
        "occupation": "Tech-support",
        "relationship": "Wife",
        "race": "White",
        "sex": "Female",
        "hours_per_week": 0,
        "native_country": "United-States",
        "capital_gain": 0,
        "capital_loss": 0
    }
    r = client.post('/predict', json=data)
    assert r.status_code == 200
    assert r.json() == {"prediction": '<=50K'}

def test_predict_greater_than_50():
    data = {
        "age": 40,
        "workclass": "Federal-gov",
        "fnlwgt": 0,
        "education": "Doctorate",
        "education_num": 16,
        "marital_status": "Married-civ-spouse",
        "occupation": "Prof-specialty",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "hours_per_week": 100,
        "native_country": "Canada",
        "capital_gain": 1000,
        "capital_loss": 0
    }
    r = client.post('/predict', json=data)
    assert r.status_code == 200
    assert r.json() == {"prediction": '>50K'}