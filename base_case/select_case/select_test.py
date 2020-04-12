# coding:utf-8
import sys

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
from busniess.select_busniess import Select_Buniess
from selenium import webdriver

import HTMLTestRunnerCN
import os
import pytest


def test_search():
    driver_ = webdriver.Chrome()
    driver_.get('https://www.baidu.com/')
    driver_.maximize_window()
    select_b = Select_Buniess(driver_)
    select_b.select_busniess()


if __name__ == '__main__':
    test_search()

