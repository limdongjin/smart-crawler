from selenium.webdriver.chrome.webdriver import WebDriver
from crawl.drivers_manager import DriversManager
from parse import parse_tables
from typing import List


class Table:

    @classmethod
    def get(cls, url) -> List[dict]:
        driver: WebDriver = DriversManager().create()
        driver.get(url)
        res: List[dict] = parse_tables(driver.page_source)
        driver.close()
        return res
