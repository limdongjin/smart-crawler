from selenium.webdriver.chrome.webdriver import WebDriver

from crawl.drivers_manager import DriversManager
from crawl.parse.xpath import parse_by_xpath


class Xpath:
    @classmethod
    def get(cls, url: str = None, xpath: str = None) -> str:
        assert url
        assert xpath

        manager: DriversManager = DriversManager()
        driver: WebDriver = manager.create()

        driver.get(url)

        return parse_by_xpath(driver.page_source, xpath)
