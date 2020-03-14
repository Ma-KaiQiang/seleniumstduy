# coding=utf-8
from util.find_element import FindElement
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait as WD
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert as AL
import unittest

'''
driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/clicks.htm')
doubleclick = driver.find_element_by_xpath("//input[@value='dbl click me']")  # 双击
click = driver.find_element_by_xpath("//input[@value='click me']")  # 单击
rightclick = driver.find_element_by_xpath("//input[@value='right click me']")  # 右键单击
db_by = (By.XPATH, "//input[@value='dbl click me']")
c_by = (By.XPATH, "//input[@value='click me']")
right_by = (By.XPATH, "//input[@value='right click me']")
# ac(driver).double_click(doubleclick).click(click).context_click(rightclick).perform()#链式

if WD(driver, 5).until(EC.title_contains('Clicks'), '页面没有正确打开，请检查'):
    print('True')
    if WD(driver, 5).until(EC.element_to_be_clickable(db_by)):
        AC(driver).double_click(doubleclick).click(click).context_click(rightclick).perform()  # 链式
else:
    driver.quit()
time.sleep(3)
driver.quit()
'''

click = driver.find_element_by_xpath("//input[@type='button']")
prompt_by = (By.XPATH, "//input[@type='button']")
check = (By.XPATH, '/html/body/h2')
input = driver.find_element_by_xpath("//input[@type='text']")
# back_by = (By.XPATH, '//a')
back = driver.find_element(By.XPATH, '//a')


class TestCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/promptTest.htm')

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        # try:
        if WD(self.driver, 5).until(EC.text_to_be_present_in_element(check, 'Prompt Test')):
            print('True')
            AC(self.driver).click(click).perform()
            time.sleep(2)
            if WD(self.driver, 5).until(EC.alert_is_present()):
                AL(self.driver).send_keys('sahai test')
                time.sleep(1)
                AL(self.driver).accept()
                if WD(self.driver, 5).until(EC.element_to_be_clickable(prompt_by)):
                    AC(self.driver).click(back).perform()
                    wu = WD(self.driver, 5).until(EC.title_is('Sahi Tests'))
                    self.assertTrue(wu)
        # except:
        #     print('运行失败')
        #     driver.quit()
        #


if __name__ == '__main__':
    ut = unittest.TestSuite()
    ut.addTest(TestCase('test_01'))
    time.sleep(5)
