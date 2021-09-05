from _11_1_city_functions import city_country
import unittest


class CityCountryTestCase(unittest.TestCase):
    """测试函数city_country"""

    def test_city_country(self):
        """能够正确处理像 ’Hong Kong, China' 的字符串吗？"""
        cc = city_country('hong Kong', 'china')
        self.assertEqual(cc, 'Hong Kong, China')


if __name__ == '__main__':
    unittest.main()
