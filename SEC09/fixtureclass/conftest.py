import pytest

@pytest.fixture(autouse=True)
def setUp():
    print('准备工作......')
    yield
    print('清理工作......')

@pytest.fixture(scope='class')
def oneTimeSetUp():
    print('类前准备工作......')
    yield
    print('类后清理工作......')