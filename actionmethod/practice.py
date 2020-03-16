# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait as WD
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert as AL
import unittest
from util.find_element import FindElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

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


class TestCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):

    def setUp(self):
        self.driver = webdriver.Chrome()

        # self.driver.get('http://sahitest.com/demo/promptTest.htm')
        # self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        # self.driver.get('http://sahitest.com/demo/selectTest.htm')
        # self.driver.get('http://sahitest.com/demo/keypress.htm')
        # self.driver.get('http://sahitest.com/demo/reactpage/react.html'
        self.driver.get('http://sahitest.com/demo/alertTest.htm')
        self.fd = FindElement(self.driver)

    def tearDown(self):
        self.driver.quit()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    # 提示框操作
    def test_01(self):
        if WD(self.driver, 10).until(
                EC.text_to_be_present_in_element(self.fd.get_located('check', 'Node1', 'practice_element.ini'),
                                                 'Prompt Test')):
            print('True')
            AC(self.driver).click(self.fd.get_element('click', 'Node1', 'practice_element.ini')).perform()
            time.sleep(2)
            if WD(self.driver, 5).until(EC.alert_is_present()):
                AL(self.driver).send_keys('sahai test')
                time.sleep(1)
                AL(self.driver).accept()
                if WD(self.driver, 5).until(
                        EC.element_to_be_clickable(self.fd.get_located('prompt_by', 'Node1', 'practice_element.ini'))):
                    AC(self.driver).click(self.fd.get_element('back', 'Node1', 'practice_element.ini')).perform()
                    wu = WD(self.driver, 5).until(EC.title_is('Sahi Tests'))
                    self.assertTrue(wu)

    # 拖拽
    def test_02(self):
        find_dragme = self.fd.get_element('dragme', 'Node2', 'practice_element.ini')
        find_ltem1 = self.fd.get_element('ltem1', 'Node2', 'practice_element.ini')
        find_ltem4 = self.fd.get_element('ltem4', 'Node2', 'practice_element.ini')
        locator_ltem1 = self.fd.get_located('ltem1', 'Node2', 'practice_element.ini')
        if WD(self.driver, 10).until(EC.title_is('Mootools Drag and Drop Example')):
            if WD(self.driver, 10).until(EC.visibility_of_element_located(locator_ltem1)):
                AC(self.driver).drag_and_drop(find_dragme, find_ltem1).perform()
                time.sleep(2)
                AC(self.driver).drag_and_drop(find_dragme, find_ltem4).perform()
                time.sleep(2)
                text = WD(self.driver, 5).until(EC.text_to_be_present_in_element(locator_ltem1, 'dropped'))
                self.assertTrue(text, '用例失败')

    # select_practice
    def test_03(self):
        select1_element = self.fd.get_element('select1', 'Node3', 'practice_element.ini')
        select2_element = self.fd.get_element('select2', 'Node3', 'practice_element.ini')
        select3_element = self.fd.get_element('select3', 'Node3', 'practice_element.ini')
        select_element = self.fd.get_element('select', 'Node3', 'practice_element.ini')
        # 假如下拉类型不是select则需要二次定位法来选择各个选项
        # element_s = self.fd.get_element('select', 'Node3', 'practice_element.ini')
        # element_s.find_element_by_xpath('//*[@id="s2Id"]/option[3]').click()
        if WD(self.driver, 10).until(EC.visibility_of(select1_element)):
            Select(select1_element).select_by_index(1)
            time.sleep(1)
            Select(select2_element).select_by_value('o2')
            time.sleep(1)
            Select(select3_element).select_by_visible_text('o3')
            time.sleep(1)
            # Select(select_element).first_selected_option()
            # Select(select1_element).deselect_by_index(1)
            # Select(select_element).all_selected_options()
            # a=EC.element_selection_state_to_be(select1_element,WE.is_selected())
            time.sleep(3)
        # self.assertTrue(result)

    # key press
    def test_04(self):
        see_located = self.fd.get_located('SeeResult', 'Node4', 'practice_element.ini')
        enter_here = self.fd.get_element('EnterHere', 'Node4', 'practice_element.ini')
        check_submit = self.fd.get_element('CheckSubmit', 'Node4', 'practice_element.ini')
        submit = self.fd.get_element('Submit', 'Node4', 'practice_element.ini')
        keyup = self.fd.get_element('KeyUp', 'Node4', 'practice_element.ini')
        keypress = self.fd.get_element('KeyPress', 'Node4', 'practice_element.ini')
        if WD(self.driver, 10).until(EC.visibility_of_element_located(see_located), '有效时间内没有进入页面'):
            AC(self.driver).send_keys_to_element(enter_here, '大家好').send_keys_to_element(check_submit, 'qiehuan').click(
                submit).perform()
            time.sleep(2)
            AC(self.driver).key_down(Keys.CONTROL, enter_here).send_keys('a').key_up(Keys.CONTROL).send_keys(
                Keys.BACKSPACE).send_keys('new').perform()
            if WD(self.driver, 10).until(EC.visibility_of(keyup)):
                AC(self.driver).click(keyup).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER).perform()
                time.sleep(2)
                result = keypress.is_selected()
                self.assertTrue(result)
                time.sleep(2)

    # alter test



if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestCase('test_05'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
