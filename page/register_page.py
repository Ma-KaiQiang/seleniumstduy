# coding:utf-8
import sys

sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")
from poium import Page, PageElement


class RegisterPage(Page):
    user_name = PageElement(xpath='//input[@name="username"]', log=True, describe='用户名')
    user_password = PageElement(xpath='//input[@name="password"]', log=True, describe='密码')
    user_name_error = PageElement(xpath='//*[@id="errormsg"]', log=True, describe='用户名错误提示信息')
    user_password_error = PageElement(xpath='//*[@id="msg"]', log=True, describe='密码错误提示信息')
    user_login_button=PageElement(css='#submit_login',log=True,describe='登录按钮')

    # def get_email_element(self):
    #     return self.fd.get_element('user_email')
    #
    # def get_username_element(self):
    #     return self.fd.get_element('user_name')
    #
    # def get_password_element(self):
    #     return self.fd.get_element('user_password')
    #
    # def get_code_element(self):
    #     return self.fd.get_element('code_text')
    #
    # def get_button_element(self):
    #     return self.fd.get_element('user_button')
    #
    # def get_email_error_element(self):
    #     return self.fd.get_element('user_email_error')
    #
    # def get_username_error_element(self):
    #     return self.fd.get_element('user_name_error')
    #
    # def get_password_error_element(self):
    #     return self.fd.get_element('user_password_error')

    # def get_code_error_element(self):
    #     return self.fd.get_element('user_code_error')

#
# if __name__=='__main__':
#     driver=webdriver.Chrome()
#     driver.get('https://sso.kedacom.com')
#     r=RegisterPage(driver)
#     r.get_username_element().send_keys('makaiqiang@kedacom.com')
#
#     driver.quit()
