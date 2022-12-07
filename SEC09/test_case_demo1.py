import pytest
import operator

def test_demoA():
    print('测试用例函数正在运行......')

def test_demoB():
    print('测试用例函数2正在运行.......')

def test_add():
    assert operator.add(5,3)==9

if __name__ == '__main__':
    pytest.main()