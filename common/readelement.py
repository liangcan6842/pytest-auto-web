#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8
# @Time   : 2022/11/1 18:46
# @Author : 梁灿

import os,sys
import yaml
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
from config.config import cm


class Element(object):
    """获取元素"""

    def __init__(self,name):
        self.file_name = '%s.yml' % name
        self.element_path = os.path.join(cm.ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='gbk') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        data = self.data.get(item)
        if data:
            name, value = data.split('==')
            return name, value
        raise ArithmeticError("{}中不存在关键字：{}".format(self.file_name, item))


# if __name__ == '__main__':
#     overview = Element('overview')
#     print(overview['首页按钮'])
