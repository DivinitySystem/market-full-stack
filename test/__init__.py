from requests import post, delete


def login(email, password):
    base_url = 'http://127.0.0.1:5000/login'
    user_data = {"email": email, "password": password}
    token = post(base_url, json=user_data).json()['token']
    
    return token


def delete_user(token, id):
    base_url = f"http://127.0.0.1:5000/user/{id}"
    response = delete(base_url,  headers={"Authorization": 'Bearer {}'.format(token)})  
    return response