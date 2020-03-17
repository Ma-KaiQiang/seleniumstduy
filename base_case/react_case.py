# coding:utf-8
import sys

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
from selenium import webdriver
import unittest
from busniess.react_buniess import ReactBusniess


class ReactCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/reactpage/react.html')
        self.react_b = ReactBusniess(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        self.assertTrue(self.react_b())


if __name__ == '__main__':
    unittest.main()
