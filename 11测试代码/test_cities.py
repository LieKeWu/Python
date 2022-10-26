import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """测试city_functions.py"""

    def test_city_country(self):
        """能处理 Hangzhou, China这样格式的信息吗？"""
        formatted_city = city_country('hangzhou', 'china')
        self.assertEqual(formatted_city, 'Hangzhou, China')


unittest.main
