from appium import webdriver

from src.functions.baseaction import BaseAction
from src.common import eleaction


class MainHome_page(BaseAction):
    """
        支付中心页面
    """
    conf = eleaction.EleAction("cfginfo.ini")
    data = eleaction.EleAction("控件.ini")
    balance = data.get_value("支付中心", "余额支付")
    payment = data.get_value("支付中心", "立即支付")
    paypwd1 = data.get_value("支付中心", "输入支付密码1")
    paypwd2 = data.get_value("支付中心", "输入支付密码2")
    paypwd3 = data.get_value("支付中心", "输入支付密码3")
    paypwd4 = data.get_value("支付中心", "输入支付密码4")
    paypwd5 = data.get_value("支付中心", "输入支付密码5")
    paypwd6 = data.get_value("支付中心", "输入支付密码6")

    def __init__(self, driver):
        super().__init__(driver)

    def click_balance(self):
        # 选择余额支付
        self.click(*self.balance)

    def click_payment(self):
        # 点击立即支付
        self.click(*self.payment)

    def Input_paypwd1(self):
        self.sendkeys(*self.paypwd1, "1")

    def Input_paypwd2(self):
        self.sendkeys(*self.paypwd2, "2")

    def Input_paypwd3(self):
        self.sendkeys(*self.paypwd1, "3")

    def Input_paypwd4(self):
        self.sendkeys(*self.paypwd1, "4")

    def Input_paypwd5(self):
        self.sendkeys(*self.paypwd1, "5")

    def Input_paypwd6(self):
        self.sendkeys(*self.paypwd1, "6")

    def payment(self):
        c = BaseAction.findelement(*self.balance)
        print(c.is_selected())


main = MainHome_page(webdriver)
main.payment()
