import requests
import json
from jsonschema import validate


def test_list_users():
    response = requests.get(url='https://reqres.in/api/users', params={'page': 2})
    assert response.status_code == 200


def test_list_users_negative():
    response = requests.get(url='https://reqres.in/api/users', params={'page': 2})
    assert response.status_code != 201


def test_create_user():
    with open('../resourses/create_user.json') as file:
        data = json.load(file)
    response = requests.post(url='https://reqres.in/api/users', json=data)
    assert response.status_code == 201


def test_update_user():
    with open('../resourses/update_user.json') as file:
        data = json.load(file)
    response = requests.put(url='https://reqres.in/api/users/2', json=data)
    assert response.status_code == 200


def test_update_user_failed():
    with open('../resourses/update_user_failed.json') as file:
        data = file.read()
    response = requests.put(url='https://reqres.in/api/users/2', json=data)
    assert response.status_code == 400


def test_delete_user():
    response = requests.delete(url='https://reqres.in/api/users/2')
    assert response.status_code == 204


def test_not_found_resourse():
    response = requests.get(url='https://reqres.in/api/unknown/23')
    assert response.status_code == 404


def test_list_users_validate():
    response = requests.get(url='https://reqres.in/api/users', params={'page': 2})
    with open('../schema/list_users.json') as file:
        data = json.load(file)
    body = response.json()
    validate(body, data)


def test_single_users_validate():
    response = requests.get(url='https://reqres.in/api/users/2')
    with open('../schema/single_user.json') as file:
        data = json.load(file)
    body = response.json()
    validate(body, data)


def test_single_res_validate():
    response = requests.get(url='https://reqres.in/api/unknown/2')
    with open('../schema/single_resource.json') as file:
        data = json.load(file)
    body = response.json()
    validate(body, data)


def test_list_res_validate():
    response = requests.get(url='https://reqres.in/api/unknown')
    with open('../schema/list_resource.json') as file:
        data = json.load(file)
    body = response.json()
    validate(body, data)
