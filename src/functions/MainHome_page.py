from src.functions.baseaction import BaseAction
from src.common import eleaction


class MainHome_page(BaseAction):
    """
        我的店铺首页页面
    """
    conf = eleaction.EleAction("控件.ini")
    data = eleaction.EleAction("数据.ini")
    mainHome = data.get_value("Tab", "本地之窗")
    goods = data.get_value("商户首页", "商品")
    shopping = data.get_value("商户首页", "加入购物车")
    pickup = data.get_value("商户首页", "自提")
    goPay = data.get_value("商户首页", "去结算")

    def click_goods(self):
        # 点击商品，进入商品详情页
        self.click(*self.goods)

    def click_shopping(self):
        # 点击加入购物车按钮
        self.click(*self.shopping)

    def click_pickup(self):
        # 选择自提
        self.click(*self.pickup)

    def click_goPay(self):
        # 点击去结算
        self.click(*self.gopay)

    def click_mainHome(self):
        # 点击本地之窗，打开本地之窗tab
        self.click(*self.mainhome)

    def shopping(self):
        """
        定义加入购物车
        :return:
        """
        self.click_mainhome()


