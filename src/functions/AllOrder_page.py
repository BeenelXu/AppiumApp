from src.functions.baseaction import BaseAction
from src.common import eleaction

class Owner_page(BaseAction):
    """
    全部订单页面
    """
    conf = eleaction.EleAction("控件.ini")
    data = eleaction.EleAction("数据.ini")