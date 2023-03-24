import unittest
from unittest.case import TestCase
from main import get_country, get_set, get_channel

class TestMain(TestCase):
    def setUp(self) -> None:
        self.geo_logs = [
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
        self.ids = {'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]}

        self.stats = {
    'facebook': 55,
    'yandex': 120,
    'vk': 115,
    'google': 99,
    'email': 42,
    'ok': 98
}

    def test_get_country(self):
        func = get_country(self.geo_logs)
        res = len(func)
        self.assertEqual(res, 6)
        
    def test_1_get_set(self):
        func = get_set(self.ids)
        res = int(len(func))
        self.assertLess(2, res)

    def test_get_channel(self):
        func = get_channel(self.stats)
        list_of_channels = ['yandex', 'ok', 'google']
        self.assertIn(func, list_of_channels)

    @unittest.expectedFailure    
    def test_get_set(self):
        func = get_set(self.ids)
        self.assertIsNone(func)
        
if __name__ == '__main__':
    unittest.main()
