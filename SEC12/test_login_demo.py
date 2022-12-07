from SEC10.POM.pages.LoginPage import LoginPage
from selenium import webdriver
import pytest
from ddt import data,unpack
from .utils.data import get_csv_data

@pytest.mark.usefixtures("oneTimeSetUp")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setUp(self,oneTimeSetUp):
        self.page = LoginPage(self.driver)


    @pytest.mark.parametrize('username,password',get_csv_data('data/users.csv'))
    @unpack
    def test_validLogin(self,username,password):
        self.page.login(username,password) #调用登录操作
        assert self.page.verify_login_successful() is True





