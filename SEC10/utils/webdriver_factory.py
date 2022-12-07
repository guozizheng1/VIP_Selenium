from selenium import webdriver

class WebDriverFactory:
    browsers={
        "firefox": lambda : webdriver.Firefox(),
        "chrome": lambda : webdriver.Chrome()
    }

    @staticmethod
    def create_driver(browser):
        # if browser.lower() == 'firefox':
        #     driver = webdriver.Firefox()
        # elif browser.lower() == 'chrome':
        #     driver = webdriver.Chrome()
        # else:
        #     driver = webdriver.Ie()

        return WebDriverFactory.browsers.get(browser,lambda : webdriver.Chrome())()