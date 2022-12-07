from selenium import webdriver
from SEC10.POM.pages.register_page import RegPage
from selenium.webdriver.common.by import By


def test_repwd_is_present():
    driver = webdriver.Chrome()
    page = RegPage(driver)

    page.open_url()

    assert page.check_repwd_is_present() is True