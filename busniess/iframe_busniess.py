# coding:utf-8
import sys

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
from page.Iframe_page import IframePage
from selenium import webdriver
import time


class IframeBusniess(IframePage):
    def __init__(self, driver):
        self.driver = driver
        super(IframeBusniess, self).__init__(driver)

    def iframe_busniess(self):
        if self.get_result(title='IFRAME Tests'):
            self.driver.switch_to_frame(self.get_ifame_element('Iframe1'))
            self.action_chains().click(self.get_ifame_element('TabletTest')).perform()
            if self.get_result(title='IFRAME Tests'):
                self.driver.switch_to_default_content()
                # self.all_delete(self.get_ifame_element('T_Input'))
                self.action_chains().send_keys_to_element(self.get_ifame_element('T_Input'), 'Hellow').click(
                    self.get_ifame_element('Click')).perform()

    def __del__(self):
        print('del')

if __name__ == '__main__':
    driver = webdriver.Chrome()

    driver.get('http://sahitest.com/demo/iframesTest.htm')
    driver.switch_to_d
    i = IframeBusniess(driver)
    i.iframe_busniess()
    time.sleep(2)
    driver.quit()
