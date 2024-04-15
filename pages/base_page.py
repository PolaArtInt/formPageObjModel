from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 15)

    def open(self):
        self.driver.get(self.url)

    def refresh(self):
        return self.driver.refresh()

    def find_elems(self, locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def find_el(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def is_visible(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_invisible(self, locator) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def visibility_of(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of(locator))

    def is_clickable(self, locator) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable(locator))
