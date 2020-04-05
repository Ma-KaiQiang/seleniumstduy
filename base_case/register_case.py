# coding=utf-8
import sys

sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")
from selenium import webdriver
import os
import HTMLTestRunnerCN
import unittest
import ddt
from until.exceluntil import ExcelUntil
from log.test_log import TestLog
from busniess.register_busniess import RegisterBusniess
from parameterized import parameterized
excel = ExcelUntil('Sheet1')


@ddt.ddt
class RegisterCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.testLog = TestLog()

    @classmethod
    def tearDownClass(cls):
        cls.testLog.close_handle()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://sso.kedacom.com')
        self.driver.maximize_window()
        self.testLog.filehandle().info('启动浏览器地址：https://sso.kedacom.com')
        self.register_b = RegisterBusniess(self.driver)

    def tearDown(self):

        errors = self._outcome.errors
        for test, exc_info in errors:
            if exc_info:
                case_name = self._testMethodName
                filename = os.path.join(os.getcwd() + '/../image/{}.png'.format(case_name))
                self.driver.save_screenshot(filename)
        self.testLog.filehandle().info('用例执行结束退出浏览器')
        self.driver.quit()

    @ddt.data(*excel.next())
    @ddt.unpack
    def test_add(self, *value):  # 使用可变参数接收序列解包的参数
        text = self.register_b.login_error(value[0], value[1], value[2])
        self.testLog.filehandle().info('输入用户名密码进行登录')
        self.assertFalse(text, value[3])


if __name__ == "__main__":
    r = RegisterCase()
    report_path = os.path.join(os.path.dirname(__file__) + '/../report/register_case.html')
    with open(report_path, 'wb')as fp:
        suite = unittest.makeSuite(RegisterCase, 'test')
        # unittest.TextTestRunner().run(suite)
        runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='test report', description='test report', verbosity=2,
                                                 tester=u'马楷强')
        runner.run(suite)
        fp.close()
