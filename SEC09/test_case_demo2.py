import pytest
import operator
from selenium import webdriver

def test_demoA():
    print('测试用例函数正在运行......')

def test_demoB():
    print('测试用例函数2正在运行.......')

def test_sub():
    assert operator.sub(5,3)==2

def test_baidu_title():
    driver = webdriver.Chrome()
    url = 'https://www.baidu.com'
    driver.get(url)
    assert '百度' in driver.title

if __name__ == '__main__':
    pytest.main()