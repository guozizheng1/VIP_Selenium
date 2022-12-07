import pytest

@pytest.fixture()
def conftestSetUp():
    print('函数级别准备工作......')
    yield
    print('函数级别清理工作......')

@pytest.fixture(scope='module')
def oneTimeSetUp():
    print('模块级别准备......')
    yield
    print('模块级别清理......')