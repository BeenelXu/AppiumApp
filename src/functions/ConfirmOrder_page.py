from src.functions.baseaction import BaseAction
from src.common import eleaction


class MainHome_page(BaseAction):
    """
        确认订单页面
    """
    conf = eleaction.EleAction("控件.ini")
    data = eleaction.EleAction("数据.ini")
    evaluate_loc = data.get_value("确认订单", "提交订单")

    def click_evaluate(self):
        # 点击提交订单
        self.click(*self.evaluate_loc)

    def evaluateOrder(self):
        # 提交订单
        self.click_evaluate()
