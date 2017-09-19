import unittest

from src.common.launchdriver import Driver
from src.functions import Login_page


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = Driver.driver()
        lg = Login_page.Login_page(self.driver)



