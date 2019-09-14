import requests
from requests import Response
from selenium.webdriver.chrome.webdriver import WebDriver


class DownLoader:
    driver: WebDriver
    selenium: bool
    site_name: str

    def __init__(self, site_name: str, selenium: bool = False, driver: WebDriver = None):
        self.site_name = site_name
        self.selenium = selenium
        self.driver = driver

    def get(self) -> str:
        if self.selenium is False:
            return self.with_request()
        else:
            return self.with_selenium()

    def with_request(self) -> str:
        res: Response = requests.get(self.site_name)
        raw_html: str = res.text

        res.close()

        return raw_html

    def with_selenium(self) -> str:
        self.driver.get(self.site_name)
        page_source = self.driver.page_source

        return page_source
