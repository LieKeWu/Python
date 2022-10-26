import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """测试city_functions.py"""

    def test_city_country(self):
        """能处理 Hangzhou, China这样格式的信息吗？"""
        formatted_city = city_country('hangzhou', 'china')
        self.assertEqual(formatted_city, 'Hangzhou, China')

    def test_city_country_population(self):
        """能处理 Hangzhou, China - population 12000000这样格式的信息吗？"""
        formatted_city = city_country('hangzhou', 'china', 12000000)
        self.assertEqual(formatted_city, 'Hangzhou, China - Population=12000000')


unittest.main
