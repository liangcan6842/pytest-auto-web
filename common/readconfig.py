#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8
# @Time   : 2022/11/1 13:19
# @Author : 梁灿

import configparser
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

from config.config import cm

HOST = 'HOST'


class ReadConfig(object):
    """配置文件"""
    def __init__(self):
       self.config = configparser.RawConfigParser()
       self.config.read(cm.ini_file, encoding='gbk')

    def _get(self,section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)


ini = ReadConfig()

# if __name__ == '__main__':
#     print(ini.url)


























