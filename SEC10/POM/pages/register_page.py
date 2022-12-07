from SEC10.POM.base.page import Page
from selenium.webdriver.common.by import By

class RegPage(Page):
    def __init__(self,driver=None,wait=10,base_url='http://115.159.224.105:8080',path='/reg/'):
        super().__init__(driver,wait,base_url,path)

    #检查某个元素是否存在
    def check_repwd_is_present(self):
        self.open_url()
        return self.is_element_present(By.ID,'pwd_confirm')




