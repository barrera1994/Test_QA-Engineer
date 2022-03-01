from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from libs.pages.googlepage import GooglePage
from libs.pages.BasePage import BasePage


def before_all(context):
    driver = set_selenium_driver()
    context.driver = driver
    context.browser = BasePage(driver, context)
    context.google = GooglePage(context)

    contexts = {
        'google': context.google,
    }
    context.all_contexts = contexts


def after_all(context):
    return context.driver.quit()


def set_selenium_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
