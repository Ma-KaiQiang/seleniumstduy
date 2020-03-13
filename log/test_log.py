# coding=utf-8
import sys

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
import logging
import time
import os


class TestLog(object):
    def __init__(self):
        self.logger1 = logging.getLogger()
        self.logger1.setLevel(logging.INFO)
        self.fmt = logging.Formatter(
            '%(asctime)s---%(filename)s---%(funcName)s---%(levelname)s---%(lineno)d---%(message)s')
        self.file_handle = logging.FileHandler(self.get_log_path())
        self.file_handle.setLevel(logging.INFO)
        self.file_handle.setFormatter(self.fmt)
        self.logger1.addHandler(self.file_handle)
        # 文件名称

    def get_name(self):
        logName = time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
        return logName

    def get_log_path(self):
        logName = self.get_name()
        logPath = os.path.join(os.path.dirname(__file__) + '/logs/' + logName)
        return logPath

    def filehandle(self):
        return self.logger1

    def streamhandle(self):
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.INFO)
        return self.ch

    def close_handle(self):
        self.logger1.removeHandler(self.file_handle)
        self.file_handle.close()

# if __name__=='__main__':
#     t=TestLog()
#     t.filehandle().debug('dajiahao')
#     t.close_handle()
