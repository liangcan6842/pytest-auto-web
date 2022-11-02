#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8
# @Time   : 2022/11/2 10:35
# @Author : 梁灿

import os, sys
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

from page.webpage import WebPage
from common.readelement import Element

login = Element('login')  # 获取login.yml


class LoginPage(WebPage):
    """登录"""
    def input_user(self, content):
        self.input_text(login['账号'], content)

    def input_pwd(self, content):
        self.input_text(login['密码'], content)

    def btn_login(self):
        self.is_click(login['登录后台'])