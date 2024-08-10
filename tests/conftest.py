import os
import pytest


@pytest.fixture()
def path_list_users_schema():
    path_list_users_schema_str = str(os.path.abspath('../schema/list_users.json'))
    return path_list_users_schema_str


@pytest.fixture()
def path_create_user_schema():
    path_create_user_schema_str = str(os.path.abspath('../schema/create_user.json'))
    return path_create_user_schema_str


@pytest.fixture()
def path_single_users_schema():
    path_single_users_schema_str = str(os.path.abspath('../schema/single_user.json'))
    return path_single_users_schema_str


@pytest.fixture()
def path_update_user_schema():
    path_update_user_schema_str = str(os.path.abspath('../schema/update_user.json'))
    return path_update_user_schema_str


@pytest.fixture()
def path_create_user():
    path_create_user_str = str(os.path.abspath('../resources/create_user.json'))
    return path_create_user_str


@pytest.fixture()
def path_update_user():
    path_update_user_str = str(os.path.abspath('../resources/update_user.json'))
    return path_update_user_str


@pytest.fixture()
def path_update_user_failed():
    update_user_failed_str = str(os.path.abspath('../resources/update_user_failed.json'))
    return update_user_failed_str
