# coding=utf-8
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
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, verbosity=2, title='测试报告', description='降维攻击测试报告', tester='马楷强')
    runner.run(run_main())
    fp.close()
