# coding=utf-8
import sys

sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")
from selenium import webdriver
import os
import HTMLTestRunnerCN
import unittest
import ddt
from util.exceluntil import ExcelUntil
from log.test_log import TestLog
from busniess.register_busniess import RegisterBusniess

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
        # self.driver.maximize_window()
        self.testLog.filehandle().info('启动浏览器地址：https://sso.kedacom.com')
        self.register_b = RegisterBusniess(self.driver)

    def tearDown(self):
        filename = os.path.join(os.getcwd() + '/../image/1.png')
        if len(self._outcome.errors) >= 1:
            self.driver.save_screenshot(filename)
        self.testLog.filehandle().info('用例执行结束退出浏览器')
        self.driver.quit()

    @ddt.data(*excel.next())
    @ddt.unpack
    def test_add(self, username, password, type, message):
        text = self.register_b.login_error(username, password, type)
        self.testLog.filehandle().info('输入用户名密码进行登录')
        self.assertFalse(text, message)


if __name__ == "__main__":
    r = RegisterCase()
    # r.main()
    # un_run=
    report_path = os.path.join(os.path.dirname(__file__) + '/../report/register_case.html')
    with open(report_path, 'wb')as fp:
        suite = unittest.makeSuite(RegisterCase, 'test')
        # unittest.TextTestRunner().run(suite)
        runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='test report', description='test report', verbosity=2,
                                                 tester=u'马楷强')
        runner.run(suite)
        fp.close()
