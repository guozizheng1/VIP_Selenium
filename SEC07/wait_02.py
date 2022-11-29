from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test():
    driver = webdriver.Chrome()
    url='http://115.159.224.105:8080/dashboard/index.html'
    driver.get(url)
    driver.maximize_window()
    wait = WebDriverWait(driver,10,0.5,ignored_exceptions='global-loader')
    flag = wait.until(EC.invisibility_of_element_located((By.XPATH,'//*[@id="global-loader"]')))
    if flag:
        menu_item = driver.find_element(By.XPATH,"//span[contains(text(),'Account')]")
        menu_item.click()

        btn_login = driver.find_element(By.XPATH,"//a[contains(text(),'Login')]")
        btn_login.click()


        try:
            email = driver.find_element(By.NAME,'email')
            email.send_keys('gzzwinner@163.com')
            print('成功')
        except:
            print('未找到元素')

if __name__ == '__main__':
    test()