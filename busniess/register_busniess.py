# coding:utf-8
import sys

sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")
from page.register_page import RegisterPage
from selenium import webdriver


class RegisterBusniess(RegisterPage):
    def __init__(self, driver):
        self.register_p = RegisterPage(driver)
        super(RegisterBusniess, self).__init__(driver)

    def login(self, username, password):
        assert self.get_title('科达云办公平台')
        self.register_p.user_name.send_keys(username)
        self.register_p.user_password.send_keys(password)
        self.register_p.user_login_button.click()

    def login_error(self, username, password, error_type, text):
        self.login(username, password)
        if error_type == '':
            if self.get_title('科达云办公'):
                return True
            return False
        result_text = getattr(self.register_p, error_type)
        if result_text.text == text:
            return True
        else:
            return False

# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     r = RegisterBusniess(driver)
#     try:
#         driver.get('https://sso.kedacom.com')
#         a = r.login_error('makaiqiang@kedacom.com', 'mkq666','','')
#         print(a)
#     except:
#         raise
#     finally:
#         driver.close()
