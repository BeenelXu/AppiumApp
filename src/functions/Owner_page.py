from src.functions.baseaction import BaseAction
from src.common import eleaction

class Owner_page(BaseAction):
    """
    我的页面
    """
    conf = eleaction.EleAction("控件.ini")
    data = eleaction.EleAction("数据.ini")
    headpic_loc = conf.get_value("个人中心", "头像")
    nickname_loc = conf.get_value("个人中心", "昵称")
    QR_loc = conf.get_value("个人中心", "二维码")
    setting_loc = conf.get_value("个人中心", "设置")
    IM_loc = conf.get_value("个人中心", "我信")
    allOrder_loc = conf.get_value("个人中心", "我的订单")
    orderUnpai_loc = conf.get_value("个人中心", "待付款")
    orderUnsent_loc = conf.get_value("个人中心", "待发货")
    orderUnreceived_loc = conf.get_value("个人中心", "待收货")
    orderService_loc = conf.get_value("个人中心", "退款/售后")
    mineWallet_loc = conf.get_value("个人中心", "我的钱包")
    shopCar_loc = conf.get_value("个人中心", "购物车")
    collectGood_loc = conf.get_value("个人中心", "收藏商品")
    careStore_loc = conf.get_value("个人中心", "店铺关注")
    mineAddress_loc = conf.get_value("个人中心", "我的地址")
    openStore_loc = conf.get_value("个人中心", "我要开店")
    wodetuiguang_loc = conf.get_value("个人中心", "我的推广")
    courier_loc = conf.get_value("个人中心", "同城快递")
    prize_loc = conf.get_value("个人中心", "推荐我连")
    choujiang_loc = conf.get_value("个人中心", "抽奖")
    prizeReCord_loc = conf.get_value("个人中心", "中奖记录")
    help_loc = conf.get_value("个人中心", "帮助与客服")
    redpacket_loc = conf.get_value("个人中心", "红包")

    def click_headpic(self):
        self.click(*self.headpic_loc)

    def click_nickname(self):
        self.click(*self.nickname)

    def click_QR(self):
        self.click(*self.QR)

    def click_setting(self):
        self.click(*self.setting_loc)

    def click_IM(self):
        self.click(*self.IM_loc)

    def click_allOrder(self):
        self.click(*self.allOrder_loc)

    def click_orderUnpai(self):
        self.click(*self.orderUnpai_loc)

    def click_orderUnsent(self):
        self.click(*self.orderUnsent_loc)

    def click_orderUnreceived(self):
        self.click(*self.orderUnreceived_loc)

    def click_orderService(self):
        self.click(*self.orderService_loc)

    def click_mineWallet(self):
        self.click(*self.mineWallet_loc)

    def click_shopCar(self):
        self.click(*self.shopCar_loc)

    def click_collectGood(self):
        self.click(*self.collectGood_loc)

    def click_careStore(self):
        self.click(*self.careStore_loc)

    def click_mineAddress(self):
        self.click(*self.mineAddress_loc)

    def click_openStore(self):
        self.click(*self.openStore_loc)

    def click_wodetuiguang(self):
        self.click(*self.wodetuiguang_loc)

    def click_courier(self):
        self.click(*self.courier_loc)

    def click_prize(self):
        self.click(*self.prize_loc)

    def click_choujiang(self):
        self.click(*self.choujiang_loc)

    def click_prizeReCord(self):
        self.click(*self.prizeReCord_loc)

    def click_help(self):
        self.click(*self.help_loc)

    def click_redpacket(self):
        self.click(*self.redpacket_loc)







