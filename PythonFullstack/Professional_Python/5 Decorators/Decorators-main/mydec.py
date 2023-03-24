import requests
import json
import os
from datetime import datetime
from functools import wraps

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            date_time = datetime.now()
            func_name = old_function.__name__
            result = old_function(*args, **kwargs)  
            with open(path,'a', encoding='utf-8') as log_file:
                log_file.write(f'Дата и время: {date_time}\n'
                        f'Имя функции: {func_name}\n'
                        f'Аргументы: {args, kwargs}\n'
                        f'Значение: {result}\n')
            return result
        return new_function
    return __logger

def _get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

heroes = {}
superheroes = ('Hulk', 'Captain America', 'Thanos')

@logger('result.log')
def most_power(url):
    r = requests.get(url)
    a = json.loads(r.content)
    for item in a:
        if item['name'] in superheroes:
            heroes[item['name']] = int(item['powerstats']['intelligence'])
    genius = max(heroes.values())
    name = _get_key(heroes, genius)
    print(f'The most intelligent superhero is {name}. Score - {genius}!')
    return heroes
    
if __name__ == '__main__':
     most_power('https://akabab.github.io/superhero-api/api//all.json')
  