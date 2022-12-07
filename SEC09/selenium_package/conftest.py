import pytest
from selenium import webdriver

#自定义命令参数--browser
def pytest_addoption(parser):
    parser.addoption("--browser")

#构造一个browser函数配置参数--browser
@pytest.fixture(scope="session")#作用域为session会话，每一次请求相当于建立一个会话机制
def browser(request):
    return request.config.getoption("--browser")

#setup准备工作里引入请求和browser浏览器
@pytest.fixture(scope='class')
def oneTimeSetUp(request,browser):
    print('setup...')
    #判断命令行的浏览器类型
    if browser=='firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    if request.cls is not None:
        request.cls.d = driver
    yield driver #获取请求的driver并返回
    print('teardown...')
    driver.quit()