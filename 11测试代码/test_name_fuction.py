import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """能够正确处理Wolfgang Amadeus Mozart这样的姓名吗？"""
        format_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus'
        )
        self.assertEqual(format_name, 'Wolfgang Amadeus Mozart')


unittest.main
