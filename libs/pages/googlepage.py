import time
from selenium.webdriver.common.by import By
from libs.pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GooglePage(object):
    def __init__(self, context):
        BasePage.__init__(self, context.browser, context)
        self.driver_2 = context.driver

    def visit_sitie(self, url):
        return self.driver.visit(url)

    def send_value_input(self, keyword):
        search_input = self.driver_2.find_element_by_name("q")
        search_input.clear()
        search_input.send_keys(keyword)

    def run_search(self):
        self.driver_2.find_element_by_name("q").submit()
        return time.sleep(5)

    def validate_query(self, quantity_results):
        list_result = WebDriverWait(self.driver_2, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#search .g a h3")))
        assert len(list_result) > int(quantity_results)
        return True

    def get_title_page(self):
        return self.driver.get_title_page()
