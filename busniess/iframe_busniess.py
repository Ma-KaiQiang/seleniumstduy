# coding:utf-8
import sys

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
from page.Iframe_page import IframePage
from selenium import webdriver
import time

class IframeBusniess(IframePage):
    def __init__(self, driver):
        self.driver = driver

        super(IframePage, self).__init__(self.driver)

    def iframe_busniess(self):
        if self.get_result(title='IFRAME Tests'):
            self.driver.switch_to_frame(self.get_ifame_element('Iframe1'))
            self.action_chains().click('TabletTest').perform()
            if self.get_result(title='Table Test'):
                self.all_delete(self.get_ifame_element('T_Input'))
                self.action_chains().send_keys_to_element(self.get_ifame_element('T_Input'), 'Hellow').click(
                    self.get_ifame_element('Click')).perform()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://sahitest.com/demo/iframesTest.htm')
    i = IframeBusniess(driver)
    i.iframe_busniess()
    time.sleep(2)
    driver.quit()