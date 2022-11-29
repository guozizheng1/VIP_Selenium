from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test():
    driver = webdriver.Chrome()
    url = 'http://115.159.224.105:8080/dashboard/login.html'
    driver.get(url)
    timestamp = round(time.time()*1000)
    filePath = 'D:\\gzz\\screenshot\\' + str(timestamp) + ".png"
    driver.save_screenshot(filePath)



test()