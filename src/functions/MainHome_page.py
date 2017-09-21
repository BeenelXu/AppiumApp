from src.functions.baseaction import BaseAction
from src.common import eleaction


class MainHome_page(BaseAction):
    """
        我的店铺首页页面
    """
    conf = eleaction.EleAction("控件.ini")
    data = eleaction.EleAction("数据.ini")
    mainHome_loc = data.get_value("Tab", "本地之窗")
    goods_loc = data.get_value("商户首页", "商品")
    shopping_loc = data.get_value("商户首页", "加入购物车")
    pickup_loc = data.get_value("商户首页", "自提")
    goPay_loc = data.get_value("商户首页", "去结算")
    shopCar_loc = data.get_value("商户首页", "购物车")
    shopCount_loc =data.get_value("商户首页", "加购数量")

    def __init__(self, driver):
        super().__init__(driver)
        self.click(*self.mainHome_loc)

    def click_goods(self):
        # 点击商品，进入商品详情页
        self.click(*self.goods_loc)

    def click_shopping(self):
        # 点击加入购物车按钮
        self.click(*self.shopping_loc)

    def click_pickup(self):
        # 选择自提
        self.click(*self.pickup_loc)

    def click_goPay(self):
        # 点击去结算
        self.click(*self.goPay_loc)


    def shopping(self):
        """
        定义加入购物车
        :return:
        """
        self.click_mainhome()
        try:
            if self.shopCount == 0:
                self.click_shopping()
                self.click_goPay()
            else:
                self.click_goPay()
        except Exception as e:
            print(e)





