# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2019/03/22 QTAF自动生成

from drunlib.testcase import DrunTestCase

class HelloTest(DrunTestCase):
    '''示例测试用例
    '''
    owner = "root"
    timeout = 5
    priority = DrunTestCase.EnumPriority.High
    status = DrunTestCase.EnumStatus.Design
    
    def run_test(self):
        self.log_info("hello testcase")
        self.assert_equal(True, True)
    
class AAAATest(DrunTestCase):
    '''示例测试用例
    '''
    owner = "root"
    timeout = 5
    priority = DrunTestCase.EnumPriority.High
    status = DrunTestCase.EnumStatus.Design
    
    def run_test(self):
        self.log_info("hello testcase")
        self.assert_equal(True, True)
    
if __name__ == '__main__':
    HelloTest().debug_run()

