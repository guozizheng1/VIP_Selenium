import ddt
import operator
import pytest
import unittest

@ddt.ddt
class TestDDT(unittest.TestCase):

    #@pytest.mark.parametrize('a,b',[(5,8),(9,3),(3,2),(12,3)])
    @ddt.file_data('D:\\VIP_Selenium\\SEC12\\value.json')
    def test_gt_ten(self,a,b):
        result = operator.add(a,b)
        self.assertGreater(result,10)

if __name__ == '__main__':
    unittest.main()