from selenium.webdriver.common.by import By
from selenium import webdriver
from SEC10.POM.base.page import Page


class LoginPage(Page):
    def __init__(self,driver=None,wait=10,base_url='http://115.159.224.105:8080',path='/login/'):
        # self.driver = driver if driver else webdriver.Chrome()#灵活配置driver可以从函数里传递也可以自定义
        # self.driver.implicitly_wait(5)
        super().__init__(driver,wait,base_url,path)

    username_locator = (By.ID,'username')
    password_locator = (By.ID,'password')
    submit_locator = (By.ID,'submit')
    error_msg = (By.XPATH,'//a[contains(text(),"返回首页")]')

    def get_username(self):
        return self.driver.find_element(*self.username_locator)

    def get_password(self):
        return self.driver.find_element(*self.password_locator)

    def get_submit_btn(self):
        return self.driver.find_element(*self.submit_locator)

    def enter_username(self,username):
        return self.get_username().send_keys(username)

    def enter_password(self,password):
        return self.get_password().send_keys(password)

    def click_login_btn(self):
        return self.get_submit_btn().click()

    def get_backhome_link(self):
        self.open_url()
        return self.get_element(By.XPATH,'//a[contains(text(),"返回首页")]')


    def login(self,username,password):

        self.open_url()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()

    def verify_login_successful(self):
        self.logger.info('正在记录用户登录测试.....')
        return self.driver.title == '用户中心'

    def verify_login_failed(self):
        result = self.is_element_present(*self.error_msg)
        self.saveScreenshot('用户登录页状态')
        return result

