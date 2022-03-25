import unittestreport
import unittest
import os
import sys

case_dir_path = os.path.dirname(os.path.abspath(__file__))
root_dir_path = os.path.dirname(case_dir_path)
sys.path.insert(0, root_dir_path)

# 是测试套件
suite = unittest.defaultTestLoader.discover(r'D:\Project\driver_demo\case', pattern='*.py')
# 创建一个用例运行程序
runner = unittestreport.TestRunner(
    suite,
    filename='report.html',
    title='interface_report',
    tester='scott',
    desc='kuaidi100',
    templates=2
)
runner.run()
