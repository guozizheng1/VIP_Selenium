from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test():
    driver = webdriver.Chrome()
    url = 'http://115.159.224.105:8080/dashboard/switch.html'
    driver.get(url)
    btn_window = driver.find_element(By.ID,'btn1')
    btn_window.click()

    login_window = driver.window_handles[1]
    driver.switch_to.window(login_window)

    email = driver.find_element(By.NAME,'email')
    email.send_keys('test@164.com')
    print('成功')

test()