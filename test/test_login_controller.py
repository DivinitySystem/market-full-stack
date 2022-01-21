from . import delete_user
from requests import  post


login_url = "http://127.0.0.1:5000/login"

def test_invalid_data_login_route():

    
    email_not_foud_data = {"email": "notfound@gmail.com", "password": "pass"} 
    user_post_email_not_found = post(login_url, json=email_not_foud_data)

    assert user_post_email_not_found.status_code == 404
    assert user_post_email_not_found.json()['error'] == "User not found"
    
    missing_keys = {}
    login_missing_keys = post(login_url, json=missing_keys)

    assert login_missing_keys.status_code == 400
    assert login_missing_keys.json()['error'] == "Missing key, email and password required"
    



def test_valid_data():
    valid_data = {"email": "notfound@gmail.com", "password": "pass", "nick_name": "name"} 
    valid_login = {"email": "notfound@gmail.com", "password": "pass"} 
    
    user_id = post("http://127.0.0.1:5000/user",json=valid_data).json()['id']
    data = post(login_url, json=valid_login)
   
    
    
    assert data.status_code == 200
    assert 'token' in data.json()
    assert type(data.json()['token']) == str

    delete_user(data.json()['token'], user_id)