import requests

URL_BASE = "https://reqres.in/api/users"

HEADERS = {
    "x-api-key": "free_user_3DlMlTJEai0AWD9gw6DvADtOxi6",
}

creds = {
    'email': 'eve.holt@reqres.in',
    'password': 'cityslicka'
}

# def get_users():
#     response = requests.get(URL_BASE,headers=HEADERS)
    
#     if response.status_code == 200:
#         print(response.json())
#     else:
#         print("Error")


# get_users()


# def login_post():
#     result = requests.post(URL_BASE,headers=HEADERS,json=creds )
#     success = result.json()
#     print(success["id"])


# login_post()


