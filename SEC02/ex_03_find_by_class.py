from selenium import webdriver
from selenium.webdriver.common.by import By

def test_find_by_class():

    driver = webdriver.Chrome('chromedriver.exe')
    url = "http://115.159.224.105:8080/dashboard/form-wizard.html"
    driver.get(url)

    driver.implicitly_wait(5)

    try:
        #input_name = driver.find_element('name','userName')
        input_name = driver.find_element(By.PARTIAL_LINK_TEXT,'Nex')
        b = input_name.text
        print('元素text值为：'+ b)
        # password
        if input_name:
            print('已找到')

    except Exception as e:
            print('未找到')


if __name__ == '__main__':
    test_find_by_class()