# coding:utf-8
import sys

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
from until.base_function import BaseFunction


class ReactPage(BaseFunction):
    def __init__(self, driver):
        self.driver = driver
        self.node = 'Node6'
        self.file_name = 'practice_element.ini'
        super(ReactPage, self).__init__(self.driver)

    def __call__(self, key):
        return self.get_element(key, self.node, self.file_name)

    def get_react_located(self, key):
        return self.get_located(key, self.node, self.file_name)
#
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get('http://sahitest.com/demo/reactpage/react.html')
#     r = ReactPage(driver)
#     text = r('Range')
#     print(text)
