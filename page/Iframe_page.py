# coding:utf-8
import sys

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
from until.base_function import BaseFunction


class IframePage(BaseFunction):
    def __init__(self, driver):
        self.driver = driver
        self.filename = 'practice_element.ini'
        self.node = 'Node7'
        super(IframePage, self).__init__(self.driver)

    def get_ifame_element(self, key,):
        print(self.node)
        return self.get_element(key, self.node, self.filename)

    def get_iframe_located(self, key):
        return self.get_located(key, self.node, self.filename)
