# coding:utf-8
import sys

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
from page.select_page import Select_Page
from poium.page_objects import PageSelect as ps


class Select_Buniess(Select_Page):
    def __init__(self, driver):
        self.driver = driver
        self.select_p = Select_Page(self.driver)
        super(Select_Buniess, self).__init__(driver)

    def select_busniess(self):
        try:

            for i in range(0, 3):
                self.select_p.move_to_element(self.select_p.search_move)
                self.select_p.search_s.click()
                ps(self.select_p.search_results, index=i)
                self.select_p.search_savebutton.click()
                assert self.select_p.get_alert_text == '已经记录下您的使用偏好', '未保存成功'
                self.select_p.accept_alert()
                self.select_p.search_input.send_keys('自动化测试')
                self.select_p.search_button.click()
                if i == 0:
                    print('2')
                    assert self.select_p.search_id10
                    print('3')
                    self.driver.back()
                elif i == 1:
                    assert self.select_p.search_id20
                    self.driver.back()
                elif i == 2:
                    assert self.select_p.search_id50
                    return True

        except:
           raise

#
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     s = Select_Buniess(driver)
#     s()
