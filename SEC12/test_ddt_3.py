import ddt
import operator
import pytest
import unittest
from .utils.utils import get_csv_data

@ddt.ddt
class TestDDT:

    #@pytest.mark.parametrize('a,b',[(5,8),(9,3),(3,2),(12,3)])
    #@ddt.file_data('D:\\VIP_Selenium\\SEC12\\value.json')
    @pytest.mark.parametrize('a,b',get_csv_data('value.csv'))#导入测试数据csv
    @ddt.unpack#由于返回的是数组嵌套需要解包
    def test_gt_ten(self,a,b):
        result = operator.add(a,b)
        assert result > 10
