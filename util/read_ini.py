# coding=utf-8
import sys

sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")
import configparser
import os



class ReadConfig(object):

    def __init__(self, ):
        self.cf = configparser.ConfigParser()
        self.filename = os.path.join(os.path.dirname(__file__) + '/../config/LocalElement.ini')
        self.node = 'LoginElement'

    def __call__(self, key, node_=None, file_name=None):

        try:
            if file_name is None:
                self.cf.read(self.filename)
            else:
                cf1 = self.cf.read(file_name)
            if node_ is None:
                text = self.cf.get(self.node, key)
                return text
            else:
                text = self.cf.get(node_, key)
                return text
        except:
            return None

# if __name__=='__main__':
#     r=ReadConfig()
#     print(type(r('user_password')))
