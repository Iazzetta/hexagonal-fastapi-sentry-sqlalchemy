import json
from fastapi.testclient import TestClient
from src.adapters.database.postgres.schemas.user import UserSchema
from src.main.application import core_module
from src.main.credentials import Credentials

client = TestClient(core_module)

def test_api_delete_users():
    # get users
    response_user_list = client.get("/users", headers={'X-Token': Credentials.X_TOKEN.value})
    assert response_user_list.status_code == 200
    user_list = response_user_list.json()['data']
    assert type(user_list) == list

    # loop and delete
    for user in user_list:
        response_delete = client.delete(
            f"/users/delete/{user['id']}", 
            headers={'X-Token': Credentials.X_TOKEN.value}
        )
        assert response_delete.status_code == 200
        assert response_delete.json()['data'] == True

def test_api_create_users():
    response = client.post(
        "/users/create", 
        content = json.dumps({'name': 'Teste', 'email': 'teste@teste.com', 'password': '123456'}),
        headers={'X-Token': Credentials.X_TOKEN.value}
    )
    assert response.status_code == 200
    assert type(response.json()['data']) == dict
    assert response.json()['data']['name'] == 'Teste'

def test_api_list_users():
    response = client.get("/users", headers={'X-Token': Credentials.X_TOKEN.value})
    assert response.status_code == 200
    assert type(response.json()['data']) == list
    assert len(response.json()['data']) == 1