from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpCond


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(ExpCond.visibility_of_element_located(locator))

    # now it's useless, but in perspective
    def elements_are_visible(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(ExpCond.visibility_of_all_elements_located(locator))
