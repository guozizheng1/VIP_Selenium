from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

    def test_validlogin(self):

        url = 'http://115.159.224.105:8080/login/'

        self.__class__.driver.get(url)

        txt_username = self.__class__.driver.find_element(By.ID,'username')
        txt_pwd = self.__class__.driver.find_element(By.ID,'password')
        btn_submit = self.__class__.driver.find_element(By.ID,'submit')

        txt_username.send_keys('Tom')
        txt_pwd.send_keys('123456')
        btn_submit.click()

        # if driver.title == '用户中心':
        #     print('登录成功！')
        # else:
        #     print('登录失败！')

        self.assertEqual(self.__class__.driver.title,'用户中心')



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':

    unittest.main(verbosity=2)