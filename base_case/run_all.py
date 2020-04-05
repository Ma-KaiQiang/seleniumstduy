# coding=utf-8
import sys

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
import unittest
import os
import HTMLTestRunnerCN

casePath = os.path.dirname(__file__)
reportPath = os.path.join(casePath + '/../report/discover_report.html')
print(reportPath)


def run_main():
    discover = unittest.defaultTestLoader.discover(casePath, '*case.py')
    return discover


with open(reportPath, 'wb')as fp:
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, verbosity=2, title='测试报告', description='浏览器：Chrom/平台：windows',
                                             tester='makaiqiang')
    runner.run(run_main())
    fp.close()
