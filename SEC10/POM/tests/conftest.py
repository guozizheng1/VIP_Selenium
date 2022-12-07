import pytest
from selenium import webdriver
from SEC10.utils.webdriver_factory import WebDriverFactory

@pytest.fixture(scope='class')
def oneTimeSetUp(request,browser):
    driver = WebDriverFactory.create_driver(browser)
    if request.cls is not None:
        request.cls.driver  = driver

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')