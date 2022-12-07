import unittest
from selenium import webdriver

class BaiduTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('类级别的准备工作')
        cls.driver = webdriver.Chrome()


    def test_baidu_title(self):
        url = 'https://www.baidu.com/'
        BaiduTest.driver.get(url)
        print('验证百度首页的标题')
        title = self.__class__.driver.title
        self.assertEqual(title,'百度一下，你就知道')

    @unittest.skip('暂时跳过')
    def test_baidu_zhidao_title(self):
        url = 'https://zhidao.baidu.com/'
        self.__class__.driver.get(url)
        print('验证百度知道的标题')
        title = self.__class__.driver.title
        self.assertTrue('全球领先' in title)

    @classmethod
    def tearDownClass(cls):
        print('类级别的清理工作')
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=1)