from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test():
    driver = webdriver.Chrome()
    url = 'http://115.159.224.105:8080/dashboard/switch.html'
    driver.get(url)

    # btn_alert = driver.find_element(By.ID,'btn2')
    # btn_alert.click()
    #
    # a = driver.switch_to.alert
    # print(a.text)
    # a.accept()#接受alert关闭
    # print('关闭成功')

    btn_confirm = driver.find_element(By.ID,'btn3')
    btn_confirm.click()

    a = driver.switch_to.alert
    print(a.text)
    a.dismiss()#取消弹窗
    print('取消成功！')
    driver.quit()



test()