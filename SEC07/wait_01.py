from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def test_submit_button():
    driver = webdriver.Chrome()
    url = 'http://115.159.224.105:8080/dashboard/delay.html'
    driver.get(url)
    btn_delay = driver.find_element(By.ID,'btn_delay')
    btn_delay.click()

    #time.sleep(10) #休眠等待
    #driver.implicitly_wait(5.0) #隐式等待
    wait = WebDriverWait(driver,10,0.5)
    #显示等待
    btn_submit = wait.until(EC.visibility_of_element_located((By.ID,'btn_submit'))) #visibility_of_element_located函数需要传递元组()
    #btn_submit = driver.find_element(By.ID,'btn_submit')
    print(btn_submit.text)

if __name__ == '__main__':
    test_submit_button()