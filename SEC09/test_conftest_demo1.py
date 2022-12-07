import pytest
import operator


def test_demoA(conftestSetUp,oneTimeSetUp):
    print('测试用例1,函数A正在运行......')

def test_demoB(conftestSetUp):
    print('测试用例1,函数B正在运行.......')

def test_add(conftestSetUp):
    assert operator.add(5,3)==8

# if __name__ == '__main__':
#     pytest.main()