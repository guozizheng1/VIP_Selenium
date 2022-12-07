import ddt
import operator
import pytest

@ddt.ddt
class TestDDT:

    # @ddt.data((5,8),(9,3),(3,2),(12,3))
    # @ddt.unpack
    @pytest.mark.parametrize('a,b',[(5,8),(9,3),(3,2),(12,3)])
    def test_gt_ten(self,a,b):
        result = operator.add(a,b)
        assert result > 10
    @pytest.mark.parametrize('s',(87,90,67,54))
    def test_score(self,s):
        assert s > 60

