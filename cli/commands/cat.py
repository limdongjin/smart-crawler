from selenium.webdriver.chrome.webdriver import WebDriver

from cli.commands.downloader import DownLoader
from crawl.drivers_manager import DriversManager


class Cat:

    @classmethod
    def with_simple(cls, site_name: str) -> str:
        return DownLoader(site_name).get()

    @classmethod
    def with_selenium(cls, site_name: str) -> str:
        manager: DriversManager = DriversManager()

        driver: WebDriver = manager.create()
        result: str = DownLoader(site_name, selenium=True, driver=driver).get()

        return result
