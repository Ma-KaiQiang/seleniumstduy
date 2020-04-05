# coding:utf-8
import sys

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
from selenium import webdriver
from page.select_page import Select_Page
from poium.page_objects import PageSelect as ps


class Select_Buniess(Select_Page):
    def __call__(self,):
        try:
            select_p = Select_Page(self.driver)
            for i in range(0, 3):
                select_p.move_to_element(select_p.search_move)
                select_p.search_s.click()
                ps(select_p.search_results, index=i)
                select_p.search_savebutton.click()
                assert select_p.get_alert_text == '已经记录下您的使用偏好', '未保存成功'
                select_p.accept_alert()
                select_p.search_input.send_keys('自动化测试')
                select_p.search_button.click()
                if i == 0:
                    assert select_p.search_id10
                    self.driver.back()
                elif i == 1:
                    assert select_p.search_id20
                    self.driver.back()
                elif i == 2:
                    assert select_p.search_id50
                    return True

        except:
            raise


if __name__ == '__main__':
    driver = webdriver.Chrome()
    s = Select_Buniess(driver)
    s()
