from typing import Dict, List, Any, Callable

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from crawl.drivers_manager import DriversManager
from crawl.util.web_element import parse_table


class Table:

    @classmethod
    def get(cls, url):
        # url: str = "http://likms.assembly.go.kr/bill/MooringBill.do"

        driver: WebDriver = DriversManager().create()
        driver.get(url)

        tables: List[WebElement] = driver.find_elements_by_tag_name('table')

        print(list(map(parse_table, tables)))