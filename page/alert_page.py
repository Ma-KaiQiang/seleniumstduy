# coding=utf-8
import sys

sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")
from until.base_function import BaseFunction


class AlertPage(BaseFunction):
    def __init__(self, driver, node=None, file_name=None):
        self.driver = driver
        self.node = 'Node5' if (node == None) else node
        self.file_name = 'practice_element.ini' if (file_name == None) else file_name
        super(AlertPage, self).__init__(self.driver)

    def __call__(self, key):
        return self.get_element(key, self.node, self.file_name)
