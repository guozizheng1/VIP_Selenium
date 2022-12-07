import pytest
from selenium import webdriver

#@pytest.mark.usefixtures("oneTimeSetUp")
class TestBaidu:

    @pytest.fixture(autouse=True)
    def classetUp(self,oneTimeSetUp):
        self.driver = self.d #引用conftest里的dirver
        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(5)
        # yield
        # self.driver.quit()#测试完成关闭driver实例
    def test_title(self):
        #driver = webdriver.Chrome()
        url = 'https://www.baidu.com'
        self.driver.get(url)
        assert '百度一下' in self.driver.title

    def test_login(self):
        pass