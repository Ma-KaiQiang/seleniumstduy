# coding=utf-8
from page.register_page import RegisterPage
import sys
sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")


class RegisterHandle ( object ) :
    def __init__ ( self , driver ) :
        self.register_p = RegisterPage ( driver )

    # 输入邮箱地址
    def send_user_email ( self , email ) :
        self.register_p.get_email_element ( ).send_keys ( email )

    # 输入用户名
    def send_user_name ( self , username ) :
        self.register_p.get_username_element ( ).send_keys ( username )

    # 输入密码
    def send_user_password ( self , password ) :
        self.register_p.get_password_element ( ).send_keys ( password )

    # 输入验证码
    def send_user_code ( self , code ) :
        self.register_p.get_code_element ( ).send_keys ( code )

    # 点击注册按钮
    def click_register_button ( self ) :
        self.register_p.get_button_element ( ).click ( )

    # 获取注册文字错误信息
    def get_user_text ( self , info ) :
        try :
            if info == 'user_email_error' :
                text = self.register_p.get_email_error_element ( ).text
            elif info == 'user_name_error' :
                text = self.register_p.get_username_error_element ( ).text
            elif info == 'user_password_error' :
                text = self.register_p.get_password_error_element ( ).text
            elif info == 'user_code_error' :
                text = self.register_p.get_code_error_element ( ).text
        except :
            text = None
        return text


# if __name__ == '__main__' :
#     driver = webdriver.Chrome ( )
#     driver.get ( 'https://sso.kedacom.com' )
#     r = RegisterHandle ( driver )
#     r.send_user_name ( "makaiqiang@kedaocm" )
#     r.click_register_button ( )
#     time.sleep ( 5 )
#     text = r.get_user_text ( "user_name_error" )
#     print ( text )
#     time.sleep ( 5 )
#     driver.quit ( )
