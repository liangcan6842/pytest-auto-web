#!/usr/bin/env python
# coding: utf-8
# @Time   : 2022/11/2 10:47
# @Author : 梁灿

import re, os, sys
import allure
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

from tools.times import sleep
import pytest
from pytest import assume
from tools import logger
from tools.times import sleep, dt_strftime
from common.readconfig import ini
from page_object.login import LoginPage


@allure.story("测试主流程，顺利通过流程")
class TestOverview:

    @allure.step('登录')
    @pytest.fixture(scope='function')
    def login(self, drivers):
        """登录"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login.input_user('xxxxxx')
        login.input_pwd('xxxxxx')
        login.btn_login()

    @allure.step("登陆后操作")
    @pytest.mark.usefixtures('login')
    def test_01(self, drivers):
        """登陆后操作"""
        print("登陆后操作")


# pytest会自动搜索测试用例，不用在这里调用，这里只是为了单个文件调试的时候使用
# if __name__ == '__main__' :
#     pytest.main(['test_01_login.py','-s'])  # '--capture=no'
















