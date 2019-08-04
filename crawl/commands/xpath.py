from selenium.webdriver.chrome.webdriver import WebDriver

from crawl.drivers_manager import DriversManager


class Xpath:
    @classmethod
    def get(cls, url: str = None, xpath: str = None) -> str:
        assert url
        assert xpath

        manager: DriversManager = DriversManager()
        driver: WebDriver = manager.create()

        driver.get(url)
        driver.implicitly_wait(5)

        return driver.find_element_by_xpath(xpath=xpath).get_attribute('outerHTML')
