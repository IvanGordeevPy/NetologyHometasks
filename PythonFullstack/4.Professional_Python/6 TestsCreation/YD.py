import requests

TOKEN_YADISK = ' '
url = 'https://cloud-api.yandex.net/v1/disk/resources'


def create_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN_YADISK}
    create_dir = requests.api.put(url, headers=headers, params=params)
    return create_dir.status_code

