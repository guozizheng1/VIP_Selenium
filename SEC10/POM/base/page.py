from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from SEC10.utils.custom_logger import Logger
import logging
import time
import os
import pathlib

class Page:
    def __init__(self,driver=None,wait=None,base_url='http://115.159.224.105:8080',path='/'):
        self.driver = driver if driver else webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = base_url
        self.path = path
        self.logger = Logger.get_logger(logging.INFO)

    def open_url(self):
        self.driver.get(self.base_url + self.path)

    def get_title(self):
        return self.driver.title

    def saveScreenshot(self,message):
        filename = f"{message}-{round(time.time() * 1000)}.png"
        screenshot_dir = pathlib.WindowsPath("D:\\VIP_Selenium\\SEC10\\tests\\screenshots\\")
        destination_file = os.path.abspath(pathlib.WindowsPath(screenshot_dir / filename))
        try:
            self.driver.save_screenshot(destination_file)
            self.logger.info(f"保存截图 {destination_file}")
        except Exception as e:
            self.logger.error(e)

    def get_element(self,*locator):
        element = None
        try:
            element = self.driver.find_element(*locator)
            print('元素已找到')
            self.logger.info(f'元素{locator}已经找到')
        except:
            print('元素未找到')
            self.logger.info(f'元素{locator}未找到')

        return element

    def click_element(self,target):
        target.click()

    def wait_for_element(self,timeout=10,poll_frequency=0.5,*locator):
        try:
            wait = WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(locator))
            print('元素已找到')
        except:
            print('元素未找到')

        return element
    def is_element_present(self,*locator):
        try:
            element = self.get_element(*locator)
            if element:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            print('元素未找到')


    def dispose(self):
        self.driver.quit()

