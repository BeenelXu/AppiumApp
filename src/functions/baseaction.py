from selenium.webdriver.support.wait import WebDriverWait


class BaseAction(object):
    """对元素操作的公共方法进行封装，并增加日志记录处理"""
    def __init__(self, driver):
        self.driver = driver

    def findelement(self, *loc):
        """查询页面元素，增加显性时间等待机制
        Args：
            *loc:定位的元素
        Retruns:
            ele(webElement):返回webelement
        """

        from selenium.common.exceptions import TimeoutException
        try:
            WebDriverWait(self.driver,15).until(lambda  driver:driver.find_element(*loc))
            ele = self.driver.find_element(*loc)
        except TimeoutException as e:
            print(e)
        return ele

    def findelements(self, *loc):
        """查询页面元素，增加显性时间等待机制
        Args：
            *loc:定位的元素组
        Retruns:
            ele(webElement):返回webelement
        """

        from selenium.common.exceptions import TimeoutException
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_elements(*loc))
            ele = self.driver.find_elements(*loc)
        except TimeoutException as e:
            print(e)
        return ele

    def isexist(self, *loc):
        """判断元素是否存在"""
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_elements(*loc))
            Exist = True
        except TimeoutError:
            Exist = False
            print("查找元素超时")
        return Exist

    def click(self, *loc):
        """click操作"""
        ele = self.findelement(*loc)
        ele.click()

    def sendkeys(self, *loc, value):
        """send_keys操作"""
        ele = self.findelement(*loc)
        ele.clear
        ele.send_keys(value)

