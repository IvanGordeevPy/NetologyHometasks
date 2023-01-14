from pprint import pprint
import requests
import json

def _get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

heroes = {}
superheroes = ('Hulk', 'Captain America', 'Thanos')
def most_power(url):
    r = requests.get(url)
    a = json.loads(r.content)
    for item in a:
        if item['name'] in superheroes:
            heroes[item['name']] = int(item['powerstats']['intelligence'])
    genius = max(heroes.values())
    name = _get_key(heroes, genius)
    print(f'The most intelligent superhero is {name}. Score - {genius}!')



class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, path_to_file):
        href = self._get_link(disk_file_path=path_to_file).get("href", "")
        response = requests.put(href, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")



if __name__ == '__main__':
    print('\nЗадание 1')
    most_power('https://akabab.github.io/superhero-api/api//all.json')
    print('\nЗадание 2')
    path_to_file = input('Введите путь до файла: ')
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)