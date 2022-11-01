#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022/11/1 19:12
# @Author : 梁灿

"""selenium基类，存放selenium基类封装方法"""

from selenium.webdriver.support import expected_conditions as EXC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
from config.config import cm
from tools.time import sleep
from tools import logger


class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            logger.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或者网址" % url)

    @staticmethod
    def element_locater(func, locator):
        """元素定位器"""
        name, value = locator
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return WebPage.element_locater(lambda *args: self.wait.until(
            EXC.presence_of_element_located(args)), locator) # presence_of_element_located((By.ID,"acdid")) 显式等待

    def get_attrib(self, locator, value):
        """获取元素属性"""
        logger.info("获取属性")
        ele = self.find_element(locator)
        sleep(0.5)
        return ele.get_attribute(value)
        # js 查找元素
        # js='document.querySelector("#质检表_返工单号").value'
        # self.driver.execute_script(js)

    def find_elements(self, locator):
        """查找多个相同元素"""
        return WebPage.element_locater(lambda *args: self.wait.until(
            EXC.presence_of_all_elements_located(args)), locator)

    def find_element_drag(self, locator):
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target) # 拖动到可见元素

    def elements_num(self, locator):
        """获取相同元素个数"""
        number = len(self.find_elements(locator))
        logger.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入前请清空"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        sleep(0.5)
        logger.info("输入文本：{}".format(txt))

    def input_enter(self, locator):
        """回车、tab等键入"""
        ele = self.find_element(locator)
        ele.send_keys(Keys.ENTER)

    def is_click(self, locator):
        "点击"
        self.find_element(locator).click()
        sleep(0.5)
        logger.info("点击元素：{}".format(locator))

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        logger.info("获取文本：{}".format(_text))
        return _text

    def hold_on(self, locator):
        # 定位到要悬停的页面
        move = self.find_element(locator)
        # 对定位到的元素执行悬停操作
        ActionChains(self.driver).move_to_element(move).perform()
        sleep(0.5)
        logger.info("悬停元素：{}".format(locator))

    def screen_scoll(self):
        self.driver.execute_script('window.scrollBy(0,300)')
        sleep(0.5)

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)




































