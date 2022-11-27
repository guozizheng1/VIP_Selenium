import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTmall(unittest.TestCase):

    def test_tmall_searchBox(self):
        # 定义驱动
        driver = webdriver.Chrome()

        # 窗口最大化
        driver.maximize_window()

        # 打开天猫
        driver.get("https://www.tmall.com")
        title = driver.title
        assert title == "天猫tmall.com--理想生活上天猫"

        # 找到搜索输入框
        search_box = driver.find_element(By.XPATH,'//body/div[1]/div[2]/div[2]/input[1]')
        search_box.clear()

        # 输入查找对象
        search_box.send_keys('显示器')


        # 定义搜索出来的产品 并统计个数
        products = driver.find_elements(By.XPATH,"//p[@class='productTitle']/a")
        print('共找到{}个产品项'.format(len(products)))

        # 遍历产品链接名称
        for link in products:
            print(link.text)

        # 退出关闭浏览器
        driver.quit()
