import logging

from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

logger = logging.getLogger(__name__)


class BasePage(object):

    def __init__(self, browser, context):
        self.driver = browser
        self.context = context

    def quit(self):
        self.driver.quit()

    def visit(self, url):
        if url == "":
            url = self.base_url
        self.driver.get(url)

    def find_element(self, selector) -> WebElement:
        try:
            return self.driver.find_element(selector[0], selector[1])
        except NoSuchElementException as e:
            raise e

    def find_elements(self, selector):
        try:
            return self.driver.find_elements(selector[0], selector[1])
        except NoSuchElementException as e:
            raise e

    def get_title_page(self) -> str:
        return self.driver.title
