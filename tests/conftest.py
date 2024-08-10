import os
import pytest


@pytest.fixture()
def path_list_users():
    path_list_users_str = str(os.path.abspath('../schema/list_users.json'))
    print(path_list_users_str)
    return path_list_users_str



    # path_create_user = str(os.path.abspath('schema/create_user.json'))
    #
    # path_single_users = str(os.path.abspath('schema/single_users.json'))
    # path_update_user = str(os.path.abspath('schema/update_user.json'))

