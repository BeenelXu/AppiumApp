import os
import time

from src.common import eleaction

ReadConfig = eleaction.EleAction("cfginfo.ini")


class AppiumServer(object):
    """启动、关闭AppiumServer"""

    def __init__(self):
        global cmd_start_appium, base_url, cmd_stop_appium
        cmd_start_appium = ReadConfig.get_value("appium", "star_appium")
        print(cmd_start_appium)
        base_url = ReadConfig.get_value("appium", "base_url")
        cmd_stop_appium = 'StopAppium.bat %s'
        print(cmd_stop_appium)
        if not os.path.exists("F:\AutoTestProject\WoLianTest\log"):
            os.makedirs("F:\AutoTestProject\WoLianTest\log")

    def start_sever(self):
        """启动AppiumServer"""
        # TODO:目前只是单一手机测试，如果是多个手机，要增加多个端口
        # cmd = 'star / b appium -a 127.0.0.1 -p 4723'
        appium_log_path = "F:\AutoTestProject\WoLianTest\log" + "appium.log"
        os.subprocess.call(cmd_start_appium, shell=True, status=open(appium_log_path, 'w'), stderr=os.subprocess.STDOUT)
        time.sleep(4)
        if self.is_running():
            print("启动appiumServer成功")
        else:
            print("启动appiumServer失败")

    def stop_Appium(self):
        p = os.popen(cmd_stop_appium)
        print(p.read())
        time.sleep(4)


