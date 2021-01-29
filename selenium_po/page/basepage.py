from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, base_url: WebDriver = None):
        if base_url is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
        else:
            self.driver = base_url

    def find(self, by: WebDriver, locator: str):
        return self.driver.find_element(by, locator)

    def finds(self, by: WebDriver, locator: str):
        return self.driver.find_elements(by, locator)

    def wait_for_click(self, locator, timeout=10):
        element: WebDriver = WebDriverWait(self.driver, timeout).until \
            (expected_conditions.element_to_be_clickable(locator))
        return element
