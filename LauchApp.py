import unittest

from appium.webdriver import webdriver

from src.common import eleaction
from src.functions import baseaction

DesireCaps = eleaction.EleAction("cfginfo.ini")
Ele = eleaction.EleAction("控件.ini")
BaseAction = baseaction.BaseAction(webdriver)

class LauchApp(unittest.TestCase):

    def setup(self):
        """初始化app driver"""
        desired_caps = {}
        desired_caps['platformName'] = DesireCaps.get_value("desired_caps_01", "platformName")  # Android
        desired_caps['platformVersion'] = DesireCaps.get_value("desired_caps_01", "platformVersion")  # android 版本
        desired_caps['deviceName'] = DesireCaps.get_value("desired_caps_01", "deviceName")  # 设备名称
        desired_caps['appPackage'] = DesireCaps.get_value("desired_caps_01", "appPackage")  # 包名
        desired_caps['appActivity'] = DesireCaps.get_value("desired_caps_01", "appActivity")  # activity名称
        base_url = DesireCaps.get_value("appium", "base_url")
        self.desired_caps = desired_caps
        self.base_url = base_url
        self.base_url = DesireCaps.get_value("appium", "base_url")
        self.driver = webdriver.Remote('self.base_url', 'self.desired_caps')

    def test_Launch(self):
        # 启动app
        Tiyan_001 = Ele.get_value("Lauch", "立即体验")
        Tiyan = BaseAction.findelement("id", Tiyan_001)
        Tiyan.click()

    def tearDown(self):
        self.driver.quite()


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()




