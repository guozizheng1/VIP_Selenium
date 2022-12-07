import unittest
import sys
import os
import ddt
import operator

@ddt.ddt
class TestDDT(unittest.TestCase):

    # @ddt.data((5,8),(9,3),(3,2),(12,3))
    # @ddt.unpack
    # def test_gt_ten(self,a,b):
    #     result = operator.add(a,b)
    #     self.assertGreater(result,10)
    @ddt.data(90,68,78,55)
    def test_score(self,s):
        self.assertGreaterEqual(s,60)

if __name__ == '__main__':
    sys.path.append(os.path.dirname(sys.path[0]))
    unittest.main()