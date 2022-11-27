from selenium import webdriver


def test_find_by_id_name():

    driver = webdriver.Chrome('chromedriver.exe')
    url = "http://115.159.224.105:8080/dashboard/form-wizard.html"
    driver.get(url)

    driver.implicitly_wait(5)

    try:
        #input_name = driver.find_element('name','userName')
        input_name = driver.find_element('css selector',"input[placeholder='Search']")
        # password
        if input_name:
            print('已找到')

    except Exception as e:
            print('未找到')


if __name__ == '__main__':
    test_find_by_id_name()