# coding=utf-8
import sys

sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")
from handle.register_handle import RegisterHandle


class RegisterBusniess():

    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, name, password):
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.click_register_button()

    def login_error(self, name, password, type):
        self.user_base(name, password)
        if self.register_h.get_user_text(type) == None:
            return True
        else:
            return False
# if __name__=="__main__":
#     driver=webdriver.Chrome()
#     driver.get('https://sso.kedacom.com')
#     r=RegisterBusniess(driver)
#     r.login_error('makaiqiang','mkq666','user_email_error')
