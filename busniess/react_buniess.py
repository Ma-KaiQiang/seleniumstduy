# coding : utf-8
import sys

sys.path.append(r'D:\student\pycharm\��Ŀ\seleniumstduy')
from page.react_page import ReactPage
from base_function import BaseFunction
from selenium.webdriver.common.keys import Keys


class ReactBusniess(BaseFunction):
    def __call__(self):
        if self.get_result(title='React Test'):
            react_page = ReactPage(self.driver)
            self.action_chains().click(react_page('Date')).send_keys('17', Keys.LEFT, Keys.UP, Keys.LEFT,
                                                                     Keys.UP).perform()
            result = self.get_result(text='2020-01-17')
            if result(react_page.get_react_located('DateText')):
                self.action_chains().drag_and_drop_by_offset(react_page('Range'), 100, 0).perform()
                result = self.get_result(text='100')
                if result(react_page.get_react_located('Text')):
                    self.action_chains().move_to_element_with_offset(react_page('Number'), 153, 8).click().send_keys(
                        '20').perform()
                    result = self.get_result(text='20')
                    if result(react_page.get_react_located('NumberText')):
                        return True

        return False

            # result=self.get_result(text='100')
            # return result(ReactPage('Text'))


# if __name__ == '__main__':
    # driver = webdriver.Chrome()
    # driver.get('http://sahitest.com/demo/reactpage/react.html')
    # driver.maximize_window()
    # r = ReactBusniess(driver)
    # result = r()
    # print(result)
    # driver.quit()
    # r=ReactBusniess()
# if  WD(driver,5).until(EC.title_is('React Test')):
#
#     AC(driver).(1327,148).click().perform()
#     time.sleep(3)
#     driver.quit()
