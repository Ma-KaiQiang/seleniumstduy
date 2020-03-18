# coding:utf-8
import sys

sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")
from until.base_function import BaseFunction
from page.alert_page import AlertPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert as al
import time


class AlterBusniess(BaseFunction):
    def __init__(self, driver):
        self.driver = driver
        self.alter_p = AlertPage(self.driver)
        super(AlterBusniess, self).__init__(self.driver)

    def __call__(self):

        if self.get_result(title='Alert Test'):
            self.action_chains().key_down(Keys.CONTROL, self.alter_p('Input')).send_keys('a').key_up(
                Keys.CONTROL).send_keys(
                Keys.BACKSPACE).send_keys_to_element(self.alter_p('Input'), 'test').click(
                self.alter_p('ClickForAlert')).perform()
        if self.get_result(alter='1'):
            method=self.alert_('accept')
            text = self.alert_('text')
            method()
            return text
