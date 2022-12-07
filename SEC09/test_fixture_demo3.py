import pytest
import operator

#@pytest.yield_fixture()
@pytest.fixture(scope='module')#声明作用范围是模块当前这个py文件
def setup():
    print('测试前的准备工作')
    yield
    print('测试后的清理工作')

def test_demoA(setup):
    print('测试用例函数正在运行......')

def test_demoB(setup):
    print('测试用例函数2正在运行.......')

def test_add(setup):
    assert operator.add(5,3)==8

# if __name__ == '__main__':
#     pytest.main()