from appium import webdriver

from src.common import eleaction

DesireCaps = eleaction.EleAction("cfginfo.ini")


class AppLaunch:


    def Launch(self):
        desired_caps = {}
        desired_caps['platformName'] = DesireCaps.get_value("desired_caps_01", "platformName")  # Android
        desired_caps['platformVersion'] = DesireCaps.get_value("desired_caps_01", "platformVersion")  # android 版本
        desired_caps['deviceName'] = DesireCaps.get_value("desired_caps_01", "deviceName")  # 设备名称
        desired_caps['appPackage'] = DesireCaps.get_value("desired_caps_01", "appPackage")  # 包名
        desired_caps['appActivity'] = DesireCaps.get_value("desired_caps_01", "appActivity")  # activity名称
        appium_url = DesireCaps.get_value("appium", "base_url")
        driver = webdriver.Remote(appium_url, desired_caps)
        driver.find_element_by_name("立即体验")
        driver.quit()
driver.find_element_by_id("com.hsmja.royal_home:id/btn_mine").click()
driver.find_element_by_id("com.hsmja.royal_home:id/nameTv").click()
driver.send_keys("13554815604")
driver.send_keys("xuyuan123456")
driver.find_element_by_id("com.hsmja.royal_home:id/tv_login").click()



launch = AppLaunch()
launch.Launch()