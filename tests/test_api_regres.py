import requests
import json
from jsonschema import validate
from path import path_resources, path_schemas


def test_list_users():
    response = requests.get(url='https://reqres.in/api/users', params={'page': 2})
    with open(f'{path_schemas('list_users.json')}') as file:
        data_validate = json.load(file)
    body = response.json()
    validate(body, data_validate)
    assert response.status_code == 200


def test_list_users_negative():
    response = requests.get(url='https://reqres.in/api/users', params={'page': 2})
    assert response.status_code != 201


def test_create_user():
    with open(f'{path_resources('create_user.json')}') as file:
        data_in = json.load(file)
    response = requests.post(url='https://reqres.in/api/users', json=data_in)
    with open(f'{path_schemas('create_user.json')}') as validate_file:
        data_validate = json.load(validate_file)
    body = response.json()
    validate(body, data_validate)
    assert response.status_code == 201


def test_update_user():
    with open(f'{path_resources('update_user.json')}') as file:
        data = json.load(file)
    response = requests.put(url='https://reqres.in/api/users/2', json=data)
    with open(f"{path_schemas('update_user.json')}") as validate_file:
        data_validate = json.load(validate_file)
    body = response.json()
    validate(body, data_validate)
    assert response.status_code == 200


def test_single_user_validate():
    response = requests.get(url='https://reqres.in/api/users/2')
    with open(f'{path_schemas('single_user.json')}') as file:
        data = json.load(file)
    body = response.json()
    validate(body, data)
    assert response.status_code == 200


def test_update_user_failed():
    with open(f'{path_resources('update_user_failed.json')}') as file:
        data = file.read()
    response = requests.put(url='https://reqres.in/api/users/2', json=data)
    assert response.status_code == 400


def test_delete_user():
    response = requests.delete(url='https://reqres.in/api/users/2')
    assert response.status_code == 204


def test_not_found_resource():
    response = requests.get(url='https://reqres.in/api/unknown/23')
    assert response.status_code == 404
    assert response.json() == {}