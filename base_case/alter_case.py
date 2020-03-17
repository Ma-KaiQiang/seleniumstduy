# coding=utf-8
import sys

sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")
from selenium import webdriver
from busniess.alter_busniess import AlterBusniess
import unittest


class AlterCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/alertTest.htm')
        self.driver.maximize_window()
        self.alter_b = AlterBusniess(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_01(self):
        text = self.alter_b()
        self.assertTrue(text, '不匹配')


if __name__ == '__main__':
    unittest.main()
