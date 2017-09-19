from src.functions.baseaction import BaseAction
from src.common import eleaction


class Login_page(BaseAction):
    """
    登录页面
    """
    conf = eleaction.EleAction("控件.ini")
    data = eleaction.EleAction("数据.ini")
    user_loc = conf.get_value("登陆", "用户名")
    user_value = data.get_value("个人帐号", "用户名")
    pwd_loc = conf.get_value("登陆", "密码")
    pwd_value = data.get_value("个人帐号", "密码")
    login_loc = conf.get_value("登陆", "立即登录")
    launch_loc = conf.get_value("启动", "立体验")

    def Launch(self):
        self.click(*self.launch_loc)

    def Input_User(self):
        self.send_keys(*self.user_loc, value=self.username_value)

    def Input_Pwd(self):
        self.sendkeys(*self.pwd_loc, value=self.pwd_value)

    def click_login(self):
        self.click(*self.login_loc)
