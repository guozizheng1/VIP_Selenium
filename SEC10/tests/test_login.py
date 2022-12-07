from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTest:


    def test_validlogin(self):

        driver = webdriver.Chrome()

        url = 'http://115.159.224.105:8080/login/'

        driver.implicitly_wait(5)

        driver.get(url)

        txt_username = driver.find_element(By.ID,'username')
        txt_pwd = driver.find_element(By.ID,'password')
        btn_submit = driver.find_element(By.ID,'submit')

        txt_username.send_keys('Tom')
        txt_pwd.send_keys('123456')
        btn_submit.click()

        if driver.title == '用户中心':
            print('登录成功！')
        else:
            print('登录失败！')

        driver.quit()

if __name__ == '__main__':

    lt = LoginTest()
    lt.test_validlogin()