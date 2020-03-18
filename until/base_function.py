# coding:utf-8
import sys

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from until.read_ini import ReadConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time


class FindElement():
    def __init__(self, driver):
        self.driver = driver
        self.al = Alert(self.driver)
    # 获取元素
    def get_located(self, key, node=None, filename=None):
        rd = ReadConfig()
        data = rd(key, node, filename)
        value = data.split(':')
        try:
            if value[0] == 'id':
                return (By.ID, value[1])
            elif value[0] == 'name':
                return (By.NAME, value[1])
            elif value[0] == 'xpath':
                return (By.XPATH, value[1])
            elif value[0] == 'class_name':
                return (By.CLASS_NAME, value[1])
        except:

            return None

    # 获取已定位元素
    def get_element(self, key, node=None, filename=None):
        gl = self.get_located(key, node, filename)
        return self.driver.find_element(gl[0], gl[1])


class BaseFunction(FindElement):

    # 动作链
    def action_chains(self, ):
        ac = ActionChains(self.driver)
        return ac

    # 警告弹框操作
    def alert_(self, func, value=None):
        method=getattr(self.al, func)
        return method
    # 全选删除
    def all_delete(self, element):
        self.action_chains().key_down(Keys.CONTROL, element).send_keys('a').key_up(Keys.CONTROL).send_keys(
            Keys.DELETE).perform()

    # 获取操作结果
    def get_result(self, title=None, getElement=None, text=None, alter=None):

        '''
        执行结果判断
        :param title:
        :param getElement:
        :return:
        '''
        ec = expected_conditions
        wdw = WebDriverWait(self.driver, 5, 0.5)
        if title is not None:
            expected_title = ec.title_is(title)
            return wdw.until(expected_title)

        elif getElement is not None:
            expected_element = ec.visibility_of(self.get_element(getElement))
            return wdw.until(expected_element)

        elif text is not None:
            def element(located):
                try:
                    return wdw.until(ec.text_to_be_present_in_element(located, text))
                except:
                    print('与预期结果不相等，或者超时')
                    return False

            return element
        elif alter is not None:
            return wdw.until(ec.alert_is_present())
