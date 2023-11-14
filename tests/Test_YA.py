import requests
import pytest


def create_folder(folder_name, access_token):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        "Authorization": f"OAuth {access_token}"
    }
    params = {
        "path": f"/{folder_name}"
    }
    response = requests.put(url, headers=headers, params=params)
    return response


def test_create_folder():
    folder_name = "Test4"
    access_token = "Your token"

    response = create_folder(folder_name, access_token)
    assert response.status_code == 201

    # Проверяем, что папка появилась в списке файлов
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        "Authorization": f"OAuth {access_token}"
    }
    params = {
        "path": "/"
    }
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200
    response_json = response.json()
    assert "_embedded" in response_json
    assert any(item["name"] == folder_name for item in response_json["_embedded"]["items"])