# coding:utf-8
import pytest
from selenium import webdriver
from busniess.register_busniess import RegisterBusniess





@pytest.fixture()
def driver_():
    driver = webdriver.Chrome()
    print('打开浏览器')
    yield driver
    print('关闭浏览器')
    driver.quit()


# @pytest.mark.parametrize('excel_case',)
# def get_excel_case(excel_case):
#     return excel_case
