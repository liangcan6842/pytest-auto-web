#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8
# @Time   : 2022/11/2 11:52
# @Author : 梁灿

import sys
import subprocess
from tools.send_mail import send_report

WIN = sys.platform.startswith('win')


def main():
   """主函数"""
   steps = [
       "pytest-auto-web\\report\\activate" if WIN else "source /bin/activate",
       "pytest --alluredir allure-results --clean-alluredir",
       "allure generate allure-results -c -o allure-report",
       "allure open allure-report"
   ]
   for step in steps:
       subprocess.run("call " + step if WIN else step, shell=True)


if __name__ == "__main__":
    send_report()
    main()