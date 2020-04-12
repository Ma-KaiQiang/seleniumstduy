# coding:utf-8
import sys
import pytest

sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")

from until.exceluntil import ExcelUntil
from busniess.register_busniess import RegisterBusniess as register_b

excel_obj = ExcelUntil('Sheet1')
excel_data = excel_obj.next()


@pytest.mark.parametrize('username,password,error_type,text', excel_data)
def test_add(driver_,username, password, error_type,text):
    driver_.get('https://sso.kedacom.com')
    driver_.maximize_window()
    assert register_b(driver_).login_error(username, password, error_type,text)


