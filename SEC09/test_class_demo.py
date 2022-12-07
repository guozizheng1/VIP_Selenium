import operator

class TestClassDemo:

    def test_demoA(self):
        print('这是一个测试demo1')

    def test_add(self):
        assert operator.add(5,3) == 8

