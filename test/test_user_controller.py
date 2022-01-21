from requests import  post, patch, delete
from . import delete_user, login

def test_post_data():
    url = 'http://127.0.0.1:5000/user'
    valid_data = {'nick_name': 'somevalue', 'password': 'pass', 'email': 'teste@gmail.com'}
    data = post(url,json=valid_data)

    id = data.json()['id']
    
    def test_valids_responses(**data):
        valid_response = ['id','nick_name', 'password', 'email']
        for key in data:
            if key not in valid_response:
                return False
            if key != 'id':
                if valid_data[key] != data[key]:
                    return False

        return True
    assert test_valids_responses(**data.json())
    assert data.status_code == 201
    assert type(data.json()) == dict

    token = login("teste@gmail.com", "pass")
    delete_data = delete_user(token, id)
    
    assert delete_data.status_code == 204
    

def test_wrong_data_on_post():
    url = 'http://127.0.0.1:5000/user'
    invalid_email = {"nick_name": "somevalue", "password": "pass", "email": "testegmail.com"}
    data = post(url,json=invalid_email)
    
    assert data.status_code == 400
    assert data.json()['error'] == "Invalid email, format should be equal to xxxx@xxxx.xxx.(xx)"
    assert type(data.json()) == dict

    url = 'http://127.0.0.1:5000/user'
    invalid_nick_name = {"nick_name": "aa", "password": "pass", "email": "teste@gmail.com"}
    data = post(url,json=invalid_nick_name)
    
    assert data.status_code == 400
    assert data.json()['error'] == "Nick_name should have length > 4 and be a string"
    assert type(data.json()) == dict

    missing_keys = {}
    data = post(url, json=missing_keys)

    assert data.status_code == 400
    assert data.json()["msg"] ==  "Missing or Invalid data, ['nick_name', 'email', 'password']"
    assert data.json()["Valid data"] == "['nick_name', 'email', 'password']"

    valid_obj = {'nick_name': 'somevalue123', 'password': 'pass123', 'email': 'teste123@gmail.com'}
    data = post(url, json=valid_obj)
    data_error = post(url, json=valid_obj)

    assert data_error.status_code == 409
    assert data_error.json()['error'] == "User or Email already taken"
    assert type(data_error.json()) == dict
    
    
def test_user_not_found():
    user_login = {'password': 'pass123', 'email': 'teste123@gmail.com'}
    token = login(**user_login)
    deleted_data = delete_user(token, 0)

    assert deleted_data.status_code == 404
    assert 'error' in deleted_data.json()
    assert deleted_data.json()['error'] == "User Not Found"


def test_patch_route():
    user_post = {'nick_name': 'nick_name', 'password': 'user', 'email': 'useruser@gmail.com'}
    id = post('http://127.0.0.1:5000/user', json=user_post).json()['id']

    user_login = {'password': 'user', 'email': 'useruser@gmail.com'}
    token = login(**user_login)
    patch_data = {"nick_name": "user_name"}
    response = patch(f'http://127.0.0.1:5000/user/{id}',json=patch_data, headers={"Authorization": 'Bearer {}'.format(token)})
    delete_user(token, id)
    
    assert response.status_code == 202
    assert 'nick_name' in response.json()
    assert response.json()['nick_name'] != user_post['nick_name']
    assert response.json()['nick_name'] == patch_data['nick_name']
