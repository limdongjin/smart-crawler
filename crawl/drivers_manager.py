from typing import List, Dict, Union, Optional

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from config_handler.reader import ConfigReader
from util.common import Singleton


class DriversManager(metaclass=Singleton):
    drivers: List[WebDriver]
    count: int

    def __init__(self):
        self.drivers = []
        self.count = 0

    def destroy_myself(self):
        for driver in self.drivers:
            print('del {0}'.format(driver))
            driver.quit()

    def create(self) -> WebDriver:
        driver_conf: Dict[str, Union[str, bool, Options]] = self.__configure()

        driver: webdriver.Chrome = webdriver.Chrome(driver_conf['chrome_driver_binary'],
                                                    options=driver_conf['options'])

        self.drivers.append(driver)
        self.count += 1

        return driver

    @staticmethod
    def __configure() -> Dict[str, Union[str, bool, Options]]:
        conf: Optional[Dict[str, Union[str, bool]]] = ConfigReader.get("selenium")

        options: Options = webdriver.ChromeOptions()
        options.binary_location = conf['binary_location']
        options.headless = conf['headless']
        chrome_driver_binary = conf['chrome_driver_binary']

        return {'chrome_driver_binary': chrome_driver_binary, 'options': options}
