# coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait as WD
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert as AL
from page.discover_page import DiscoverPage
from selenium.webdriver.common.keys import Keys


class AlterBusniess(object):
    def __init__(self, driver):
        self.driver = driver
        self.discover_p = DiscoverPage(self.driver)

    def alter_accept(self):

        if WD(self.driver, 10).until(EC.title_is('Alert Test')):
            AC(self.driver).key_down(Keys.CONTROL, self.discover_p('alter_input')).send_keys('a').key_up(
                Keys.CONTROL).send_keys(
                Keys.BACKSPACE).send_keys_to_element(self.discover_p('alter_input'), 'test').click(
                self.discover_p('alter_click')).perform()
            time.sleep(2)
            if WD(self.driver, 5).until(EC.alert_is_present()):
                text = AL(self.driver).text
                AL(self.driver).accept()
                return text
