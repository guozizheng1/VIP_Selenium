import pytest
import pytest_ordering

@pytest.mark.run(order=3)
def test_A():
    print('用例函数【A】')

@pytest.mark.run(order=2)
def test_B():
    print('用例函数【B】')

@pytest.mark.run(order=1)
def test_C():
    print('用例函数【C】')

@pytest.mark.run(order=4)
def test_D():
    print('用例函数【D】')

@pytest.mark.run(order=5)
def test_E():
    print('用例函数【E】')

@pytest.mark.run(order=6)
def test_F():
    print('用例函数【F】')

@pytest.mark.run()
def test_G():
    print('用例函数【G】')

@pytest.mark.run(order=8)
def test_H():
    print('用例函数【H】')