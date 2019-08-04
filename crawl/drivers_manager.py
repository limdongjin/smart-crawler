from typing import List, Dict, Union, Optional
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from config_handler.reader import ConfigReader


# [TODO] driver remove operation
class DriversManager:
    drivers: List[WebDriver]
    count: int

    def __init__(self):
        self.drivers = []
        self.count = 0

    def __del__(self):
        pass
        # for driver in self.drivers:
        #     try:
        #         driver.close()
        #     except ValueError as e:
        #         print(e)

    def create(self) -> WebDriver:
        driver_conf: Dict[str, Union[str, bool, Options]] = self.__configure()

        driver: webdriver.Chrome = webdriver.Chrome(driver_conf['chrome_driver_binary'],
                                                    chrome_options=driver_conf['options'])

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
