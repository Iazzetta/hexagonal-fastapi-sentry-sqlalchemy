import json
from fastapi.testclient import TestClient
from src.main.application import core_module
from src.main.credentials import Credentials

client = TestClient(core_module)

def test_create_users():
    response = client.post(
        "/users/create", 
        content = json.dumps({'name': 'Teste', 'email': 'teste@teste.com', 'password': '123456'}),
        headers={'X-Token': Credentials.X_TOKEN.value}
    )
    print(response.json())
    assert response.status_code == 200
    data_response = response.json()
    assert data_response['data']['name'] == 'Teste'

def test_list_users():
    response = client.get("/users", headers={'X-Token': Credentials.X_TOKEN.value})
    assert response.status_code == 200