#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8
# @Time   : 2022/11/2 10:28
# @Author : 梁灿

import os, sys
import yaml
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
from config.config import cm
from tools.times import running_time


@running_time
def check_element():
    """检查所有元素是否正确，简单的检查"""
    for files in os.listdir(cm.element_path):
        _path = os.path.join(cm.element_path, files)
        with open(_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        for k in data.values():
            try:
                pattern, value = k.split('==')
            except ValueError:
                raise Exception("{}:{} 元素表达式中没有‘==’".format(_path,k))
            if pattern not in cm.locate_mode:
                raise Exception('%s中元素[%s]没有指定类型' % (_path, k))
            else:
                assert value, '%s中元素[%s]类型与值不匹配' % (_path, k)


if __name__ == '__main__':
    check_element()



















