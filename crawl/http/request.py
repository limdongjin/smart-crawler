import requests
from selenium import webdriver
from config.selenium import config_selenium

class DownLoader:
    def __init__(self, site_name, selenium=False):
        self.site_name = site_name
        self.selenium = selenium

    def get(self):
        if self.selenium is False:
            return self.with_request()
        else:
            return self.with_selenium()

    def with_request(self):
        res = requests.get(self.site_name)
        raw_html = res.text
        res.close()

        return raw_html

    def with_selenium(self):

        options = webdriver.ChromeOptions()
        options.binary_location = config_selenium["binary_location"]
        options.headless = config_selenium["headless"]
        chrome_driver_binary = config_selenium["chrome_driver_binary"]

        driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        driver.get(self.site_name)
        page_source = driver.page_source
        driver.close()

        return page_source