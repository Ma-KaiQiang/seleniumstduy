# coding=utf-8
import unittest
from selenium import webdriver
from busniess.alter_busniess import AlterBusniess


class AlterCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/alertTest.htm')
        self.alter_b = AlterBusniess(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_01(self):
        text = self.alter_b.alter_accept()
        self.assertEqual(text, 'test', '不匹配')


if __name__ == '__main__':
    unittest.main()
