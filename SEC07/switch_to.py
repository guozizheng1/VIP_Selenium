from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test():
    driver = webdriver.Chrome()
    url = 'http://115.159.224.105:8080/dashboard/login-2.html'
    driver.get(url)

    try:
        iframe = driver.find_element(By.TAG_NAME,'iframe')
        driver.switch_to.frame(iframe)
        email = driver.find_element(By.NAME,'email')
        email.send_keys('gzzwinner@163.com')
        print('成功！')
        driver.switch_to.default_content()

    except Exception as e:
        print(e)
        print('失败')

test()