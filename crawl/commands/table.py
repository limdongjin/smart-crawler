from selenium.webdriver.chrome.webdriver import WebDriver
from crawl.drivers_manager import DriversManager
from crawl.util.web_element import parse_table


class Table:

    @classmethod
    def get(cls, url):
        driver: WebDriver = DriversManager().create()
        driver.get(url)
        res = parse_table(driver.page_source)
        return res
