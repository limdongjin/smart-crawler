from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from config_handler.reader import ConfigReader
from util.common import Singleton
from selenium.webdriver.chrome.service import Service


class DriversManager(metaclass=Singleton):
    drivers: List[WebDriver]
    chrome_options: Options
    service: Service

    def __init__(self):
        self.drivers = []
        self.chrome_options = webdriver.ChromeOptions()
        conf: dict = ConfigReader.get("selenium")

        if conf['headless']:
            self.chrome_options.add_argument('--headless')
            self.chrome_options.add_argument('--no-sandbox')
            self.chrome_options.add_argument('--disable-dev-shm-usage')

        self.service = Service(executable_path=conf['chrome_driver_binary'])

    def destroy_myself(self):
        for driver in self.drivers:
            print('del {0}'.format(driver))
            driver.quit()
        self.drivers = []

    def create(self) -> WebDriver:
        try:
            driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        except WebDriverException as e:
            print(e)
            print("Check your chromedriver path or re install.")
            assert False

        self.drivers.append(driver)

        return driver

    def count(self):
        return len(self.drivers)