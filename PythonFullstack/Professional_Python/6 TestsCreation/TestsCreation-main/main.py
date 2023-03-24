print('Задание №1')
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
def get_country(geo_logs):
    numb = 0
    logs_geo = []
    a = len(geo_logs) - 1
    while numb <= a:
        if (geo_logs[numb].get(f'visit{numb + 1}')[1]) == 'Россия':
            logs_geo.append(geo_logs[numb])
            numb += 1
        else:
            numb += 1
    geo_logs = logs_geo
    return geo_logs


ids = {'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]}
        
def get_set(ids):
    n = 1
    set_a = set(ids.get(f'user{n}'))
    while n <= len(ids):
        set_a = set_a | (set(ids.get(f'user{n}')))
        n += 1
    return set_a

stats = {
    'facebook': 55,
    'yandex': 120,
    'vk': 115,
    'google': 99,
    'email': 42,
    'ok': 98
}

def get_channel(stats):
    maximum = 1
    for a in stats.keys():
        if stats[a] > maximum:
            maximum = stats[a]
            channel = a
    return channel