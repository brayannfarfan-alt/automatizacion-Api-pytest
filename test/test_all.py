from api_client import get_users, create_user, login_user,update_users, delete_user, get_one_user
import logging
import os
import pytest_check  as check

os.makedirs("logs",exist_ok=True) #FileExistsError

logging.basicConfig(
    filename="logs/execution.log",
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s – %(message)s',
    force=True
)
logger = logging.getLogger(__name__)


def test_get_user():
    logger.info("LLAMANDO A LA API.....")
    response = get_users()
    logger.info("obtuve la respuesta")
    check.equal(response.status_code,200,"EL STATUS NO ES 200") 
    logger.error("SE Mostro UN ERROR AL COMAPRA CON EL STATUS CODE")
    # data = response.json()
    # print(data)
    # assert "data" in data
    # assert len(data["data"]) > 0


# def test_create_user( user_data ):
#     response = create_user(
#         user_data["name"],
#         user_data["job"]
#     )

    # response = cretate_user(
    #     "Bray",
    #     "Albañil"
    # )

    # assert response.status_code == 201

    # body = response.json()
    
    # assert body["name"] == "Bray"
    # assert body["job"] == "Albañil"


# def test_update_user( ):
#     response = update_users(
#         "Bray updated",
#         "QA Automation",
#         2
#     )

#     assert response.status_code == 200

#     body = response.json()

#     print(body)



# def test_delete_user():
#     response = delete_user(1)
#     assert response.status_code == 204

# def test_one_user():
#     response = get_one_user(2)
#     print(response.json())
#     assert response.status_code == 200
