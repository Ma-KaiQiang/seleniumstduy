# coding=utf-8
import sys

sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")
from util.read_ini import ReadConfig
from selenium.webdriver.common.by import By


# from selenium import webdriver


# 根据配置文件中的内容进行查找元素
class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

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

    def get_element(self, key, node=None, filename=None):
        gl = self.get_located(key, node, filename)
        return self.driver.find_element(gl[0], gl[1])

# if __name__ == '__main__' :
#     print ( '1' )
#     dr = webdriver.Chrome ( )
#     print ( '2' )
#     dr.get ( 'https://sso.kedacom.com' )
#     print ( '3' )
#     F = FindElement ( dr ).get_element ( 'user_name' )
#
#     F.send_keys ( 'makaiqiang@kedacom.com' )
#
#     dr.quit ( )
