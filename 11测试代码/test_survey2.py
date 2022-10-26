import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类进行测试"""

    def setUp(self) -> None:
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """

    question = "What language did you first learn to speak?"
    my_survery = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善存储"""
        self.my_survery.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survery.responses)

    def test_store_three_response(self):
        """测试3个答案会被妥善存储"""
        for response in self.responses:
            self.my_survery.store_response(response)
            self.assertIn(response, self.my_survery.responses)


unittest.main
