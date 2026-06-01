import requests

URL_BASE = "https://reqres.in/api"

HEADERS = {
    "x-api-key": "free_user_3DlMlTJEai0AWD9gw6DvADtOxi6",
}

creds = {
    'email': 'eve.holt@reqres.in',
    'password': 'cityslicka'
}

def get_users():
    return requests.get(
        f"{URL_BASE}/users",headers=HEADERS
    )

def create_user(name, job):
    data = {
        "name":name,
        "job":job
    }

    return requests.post(
        f"{URL_BASE}/users",headers=HEADERS, json=data
    )


def login_user(email, password):
    data = {
        "email":email,
        "password":password
    }

    return requests.post(
        f"{URL_BASE}/login", json=data, headers=HEADERS
    )

def update_users(name, job):
    data = {
        "name":name,
        "job":job
    }