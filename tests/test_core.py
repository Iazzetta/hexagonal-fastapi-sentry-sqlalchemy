from src.core.domain.user.user import User

user_test: User = {
    "name": "Test",
    "email": "test@test.com",
    "password": "123456"
}

user_list: list[User] = []

def test_core_create_user():
    user = User(
        name = user_test['name'],
        email = user_test['email'],
        password = user_test['password']
    )
    assert type(user) == User
    assert user.name == user_test['name']
    assert user.email == user_test['email']
    assert user.password == user_test['password']

    user_list.append(user)

def test_core_list_user():
    assert type(user_list) == list
    assert len(user_list) == 1
    assert user_list[0].name == user_test['name']
    assert user_list[0].email == user_test['email']
    assert user_list[0].password == user_test['password']