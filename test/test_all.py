from api_client import get_users, create_user, login_user,update_users

# def test_get_user():
#     response = get_users()
    
#     assert response.status_code == 200

#     data = response.json()
#     print(data)
#     assert "data" in data
#     assert len(data["data"]) > 0


def test_create_user( user_data ):
    response = create_user(
        user_data["name"],
        user_data["job"]
    )

    # response = cretate_user(
    #     "Bray",
    #     "Albañil"
    # )

    assert response.status_code == 201

    body = response.json()
    
    assert body["name"] == "Bray"
    assert body["job"] == "Albañil"


def update_user( user_data):
        response = update_users(
              user_data["name"]
        )