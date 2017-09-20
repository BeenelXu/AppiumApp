"""读取ini配置文件工具类"""
import codecs
import configparser

import os

prjdir = os.path.dirname(os.path.dirname((os.path.dirname(__file__))))
path = os.path.join(prjdir + '/config/')


class EleAction(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_path = path + self.file_name
        self.cf = configparser.ConfigParser()
        self.cf.read(self.file_path, 'utf-8')

    def get_value(self, session, option):
        # 读配置，返回数据
        value = self.cf.get(session, option)
        return value

    def get_eleinfo(self, session, option):
        # 读控件配置，返回一组数据
        eleinfo = self.cf.get_value(session, option)
        return eleinfo.split('|')

    def get_items(self, section):
        # 读配置文件，返回一组数组
        self.cf.read(self.file_path, 'utf-8')
        dict = self.cf.items(section)
        return dict


if __name__ == "__main__":
    value = EleAction("cfginfo.ini").get_value("appium", "star_appium")
    print(value)
