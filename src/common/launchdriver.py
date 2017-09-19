from appium import webdriver

from src.common import eleaction


def Driver():
    cfgRead = eleaction.EleAction("cfginfo.ini")
    base_url = cfgRead.get_value("appium", "base_url")
    desired_caps = dict(cfgRead.get_items("desired_caps_01"))
    print(desired_caps)
    dr = webdriver.Remote(base_url, desired_caps)
    return dr


if __name__ == "__main__":
    dr1 = Driver()
    dr1.quit()
