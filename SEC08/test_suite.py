import unittest

from SEC08.test_case_01 import MyTest
from SEC08.test_case_02 import BaiduTest

#定义case
# tc1 = unittest.TestLoader().loadTestsFromTestCase(MyTest)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(BaiduTest)

#定义测试套件集合
#suites = unittest.TestSuite([tc1,tc2])

suites = unittest.TestLoader().discover('.',pattern='test_case*.py')

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suites)