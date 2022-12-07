import pytest
import operator


def test_demoA(conftestSetUp,oneTimeSetUp):
    print('测试用例2,函数A正在运行......')

def test_demoB(conftestSetUp,oneTimeSetUp):
    print('测试用例2,函数B正在运行.......')

def test_add(conftestSetUp,oneTimeSetUp):
    assert operator.add(5,3)==8

# if __name__ == '__main__':
#     pytest.main()