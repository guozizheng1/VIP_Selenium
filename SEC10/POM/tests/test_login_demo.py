from SEC10.POM.pages.LoginPage import LoginPage
from selenium import webdriver
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setUp(self,oneTimeSetUp):
        self.page = LoginPage(self.driver)

    @pytest.mark.run(order=3)
    def test_validLogin(self):
        self.page.login('Tom','123456') #调用登录操作
        assert self.page.verify_login_successful() is True

    @pytest.mark.run(order=2)
    def test_invalid_login(self):
        self.page.login('Tom', '331')  # 调用登录操作

        assert self.page.verify_login_failed() is True

    @pytest.mark.run(order=1)
    def test_back_link(self):
        link = self.page.get_backhome_link()
        assert link is not None




