import pytest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class Test_Something:

    # @pytest.fixture(autouse=True)
    # def setUp(self):
    #     print('准备工作......')
    #     yield
    #     print('清理工作......')

    def test_method_A(self):
        print('测试类 > 用例方法 A')

    def test_method_B(self):
        print('测试类 > 用例方法 B')

    def test_method_C(self):
        print('测试类 > 用例方法 C')