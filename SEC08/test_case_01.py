import unittest
import operator

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print(f"\n{'>'*30}")
        print('类的准备工作')
        print(f"\n{'>'*30}")

    @classmethod
    def tearDownClass(cls) -> None:
        print(f"\n{'>' * 30}")
        print('类的清理工作')
        print(f"\n{'>' * 30}")

    def setUp(self):
        print(f"\n{'='*20}")
        print('一些准备工作')
        print(f"\n{'=' * 20}")

    def tearDown(self) -> None:
        print(f"\n{'=' * 20}")
        print('一些清理工作')
        print(f"\n{'=' * 20}")

    def test_add(self):  #实例方法
        print('测试加法')
        self.assertEqual(operator.add(5,3),8)

    def test_mul(self):
        print('测试乘法')
        self.assertEqual(operator.mul(5,3),15)

if __name__ == '__main__':
    unittest.main(verbosity=2)