# coding=utf-8
from util.find_element import FindElement


class DiscoverPage(object):
    def __init__(self, driver, node=None, file_name=None):
        self.driver = driver
        self.find_e = FindElement(self.driver)
        self.node = 'Node5' if (node == None) else node
        self.file_name = 'practice_element.ini' if (file_name == None) else file_name

    def __call__(self, key):
        if key == 'alter_input':
            return self.find_e.get_element('Input', self.node, self.file_name)
        elif key == 'alter_click':
            return self.find_e.get_element('ClickForAlert', self.node, self.file_name)
