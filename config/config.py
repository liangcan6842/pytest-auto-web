#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022/11/1 11:00
# @Author : 梁灿


import os,sys
from selenium.webdriver.common.by import By
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
# from tools.times import  dt_strftime


class ConfigManager(object):
    # 项目目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 页面元素目录
    element_path = os.path.join(base_dir, 'page_element')
    # 报告文件
    report_dir = os.path.join(base_dir, 'report.html')

    # 元素定位类型
    locate_mode = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class':By.CLASS_NAME
    }

    # 邮件信息
    email_info = {
        'username': '1473166229@qq.com',  # 邮箱
        'password': 'hqrgvfgcnqhobabi',  # 授权码
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }
    # 收件人
    address = ['1473166229@qq.com']

    @property  # 创建只读属性
    def log_file(self):
        """日志目录"""
        log_dir = os.path.join(self.base_dir, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir,'{}.log'.format(dt_strftime()))

    @property
    def ini_file(self):
        """配置文件"""
        ini_file = os.path.join(self.base_dir, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file


cm = ConfigManager()
if __name__ == '__main__':
    print(cm.base_dir)























