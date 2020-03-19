# coding=utf-8
import sys
from log.test_log import TestLog
sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")
from selenium import webdriver
from busniess.alter_busniess import AlterBusniess
import unittest


class AlterCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/alertTest.htm')
        # self.driver.maximize_window()
        self.test_log=TestLog()
        self.alter_b = AlterBusniess(self.driver)
    def tearDown(self):
        self.driver.close()
        self.test_log.close_handle()
        # self.close_handle()

    def test_01(self):
        text = self.alter_b()
        self.assertEqual(text, 'test')
        self.test_log.filehandle().info('执行测试用例')


if __name__ == '__main__':
    unittest.main()
