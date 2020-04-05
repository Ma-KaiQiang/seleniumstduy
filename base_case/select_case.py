# coding:utf-8
import sys

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
from busniess.select_busniess import Select_Buniess
from selenium import webdriver
import HTMLTestRunnerCN
import os
import unittest


class Select_Case(unittest.TestCase, Select_Buniess):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.select_b = Select_Buniess(cls.driver)

    def setUp(self):
        self.select_b.get('https://www.baidu.com/')
        self.driver.maximize_window()

    def test_search(self):
        self.assertTrue(self.select_b())

    def tearDown(self):
        errors = self._outcome.errors
        for test, exc_info in errors:
            if exc_info:
                case_name = self._testMethodName
                filename = os.path.join(os.getcwd() + '/../image/{}.png'.format(case_name))
                self.driver.save_screenshot(filename)
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    s = Select_Case()
    report_path = os.path.join(os.path.dirname(__file__) + '/../report/select_case.html')
    with open(report_path, 'wb') as fp:
        runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, verbosity=2, title="下拉框测试报告",
                                                 description='运行环境：Chrome/windows', tester='makaiqiang')
        suite = unittest.TestSuite()
        suite.addTest(Select_Case('test_search'))
        runner.run(suite)
        fp.close()