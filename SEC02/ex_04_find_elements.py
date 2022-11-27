from selenium import webdriver
from selenium.webdriver.common.by import By

def test_find_elements():
    driver = webdriver.Chrome("chromedriver.exe")
    url = 'http://115.159.224.105:8080/dashboard/form-wizard.html'
    driver.get(url)
    inputs = driver.find_elements(By.TAG_NAME,'input')
    print(inputs)
    print()
    type(inputs)

if __name__ == '__main__':
    test_find_elements()