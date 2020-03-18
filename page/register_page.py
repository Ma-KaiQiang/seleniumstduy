# coding=utf-8
from until.base_function import FindElement


class RegisterPage(object):
    def __init__(self, driver):
        self.fd = FindElement(driver)

    def get_email_element(self):
        return self.fd.get_element('user_email')

    def get_username_element(self):
        return self.fd.get_element('user_name')

    def get_password_element(self):
        return self.fd.get_element('user_password')

    def get_code_element(self):
        return self.fd.get_element('code_text')

    def get_button_element(self):
        return self.fd.get_element('user_button')

    def get_email_error_element(self):
        return self.fd.get_element('user_email_error')

    def get_username_error_element(self):
        return self.fd.get_element('user_name_error')

    def get_password_error_element(self):
        return self.fd.get_element('user_password_error')

    def get_code_error_element(self):
        return self.fd.get_element('user_code__error')

#
# if __name__=='__main__':
#     driver=webdriver.Chrome()
#     driver.get('https://sso.kedacom.com')
#     r=RegisterPage(driver)
#     r.get_username_element().send_keys('makaiqiang@kedacom.com')
#
#     driver.quit()
