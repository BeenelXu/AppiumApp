import unittest
from time import sleep

from src.common.launchdriver import Driver
from src.common.screenshot import screen_shot
from src.functions import Login_page


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = Driver.driver()
        lg = Login_page.Login_page(self.driver)
        lg.login()

    def tearDown(self):
        sleep(3)
        screen_shot(self.driver)
        self.driver.close_app()
        self.driver.quit()





