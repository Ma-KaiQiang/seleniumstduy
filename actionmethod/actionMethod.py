# coding=utf-8
from util.find_element import FindElement
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class ActionMethod():
    # 打开网页
    def open_browser(self, type):
        if type == 'chrome':
            self.driver = webdriver.Chrome()
            # self.driver.find_element().send_keys()
        elif type == 'firefox':
            self.driver = webdriver.Firefox()
        elif type == 'edge':
            self.driver = webdriver.Edge()

    def get_url(self, url):
        self.driver.get(url)

    # 输入
    def input(self, key, value):
        element = FindElement(self.driver).get_element(key)
        element.send_keys(value)

    # 点击
    def click(self, key):
        self.element = FindElement(self.driver).get_element(key)
        self.element.click()

    # 等待时间
    def time_sleep(self):
        time.sleep(5)

    # 关闭窗口
    def colse_browser(self):
        self.driver.quit()

    # 获取title
    def get_title(self):
        title = self.driver.title
        return title

    def action_chains(self, *args):
        self.element = FindElement(self.driver)
        self.ac = ActionChains(self.driver)

        for i in range(len(args)):
            print(args[i])
            self.click(args[i])
            # self.ac.click( self.element.get_element(args[i]))
            time.sleep(2)
        # self.ac.perform()

    def expetecd_condithon(self, title=None, getElement=None):
        ec = expected_conditions
        self.wait = WebDriverWait(self.driver, 5, 0.5)
        if title is not None:
            expected_title = ec.title_contains(title)
            self.wait.until(expected_title)

        if getElement is not None:
            getelement = FindElement(self.driver).get_element(getElement)
            expected_element = ec.visibility_of(getelement)
            self.wait.until(expected_element)




if __name__ == '__main__':
    '''
    action_chains
    # action = ActionMethod()
    # action.open_browser('chrome')
    # action.get_url('https://www.baidu.com')
    # action.action_chains('baidu_setup','search_setup', 'search11', 'search21', 'search31', 'search41', 'search_save')
    # time.sleep(4)
    # action.colse_browser()
    '''
    '''
    action = ActionMethod()
    action.open_browser('chrome')
    action.get_url('https://www.baidu.com')
    # action.expetecd_condithon('baidu_click')
    # action.input('baidu_input', '自动化测试')
    # action.click('baidu_click')
    # time.sleep(2)
    # action.colse_browser()
    '''
    action = ActionMethod()
    action.open_browser('chrome')
    action.get_url('https://www.baidu.com')
    locator=(By.ID,'su')
    EC.presence_of_element_located(locator)
    action.input('baidu_input', '自动化测试')
    action.click('baidu_click')
    time.sleep(2)
    action.colse_browser()