from time import sleep

from appium import webdriver

from src.common import eleaction
from src.functions import baseaction

Ele = eleaction.EleAction("控件.ini")
BaseAction = baseaction.BaseAction(webdriver)

desired_caps = {}
desired_caps['platformName'] = "Android"  # Android
desired_caps['platformVersion'] = "5.0"  # android 版本
desired_caps['deviceName'] = "6c024ac3"  # 设备名称
desired_caps['appPackage'] = "com.hsmja.royal_home"  # 包名
desired_caps['appActivity'] = "com.hsmja.royal.home.HomePanDuan"  # activity名称
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
sleep(5)
ele = Ele.get_value("Lauch", "立即体验")
lau = BaseAction.findelement("id", ele)
lau.click()
sleep(5)
driver.find_element_by_id("com.hsmja.royal_home:id/btn_mine").click()
sleep(5)
driver.find_element_by_id("com.hsmja.royal_home:id/nameTv").click()
sleep(5)
driver.send_keys("13554815604")
sleep(10)
ele = driver
ele.click()
ele.send_keys("xuyuan123456")
sleep(10)
driver.find_element_by_id("com.hsmja.royal_home:id/tv_login").click()
sleep(5)





