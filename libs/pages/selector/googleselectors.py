from selenium.webdriver.common.by import By

class GoogleSelectors:
    search_input = (By.NAME, 'q')
    result_query = (By.CSS_SELECTOR, 'div#search .g a h3')