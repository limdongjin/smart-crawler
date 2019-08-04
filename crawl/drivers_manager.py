from selenium import webdriver
from config_handler.reader import ConfigReader


# [TODO] driver remove operation
class DriversManager:
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

    def create(self):
        driver_conf = self.__configure()

        driver = webdriver.Chrome(driver_conf['chrome_driver_binary'],
                                  chrome_options=driver_conf['options'])

        self.drivers.append(driver)
        self.count += 1

        return driver

    def __configure(self):
        conf = ConfigReader.get("selenium")
        options = webdriver.ChromeOptions()
        options.binary_location = conf['binary_location']
        options.headless = conf['headless']
        chrome_driver_binary = conf['chrome_driver_binary']

        return {'chrome_driver_binary': chrome_driver_binary, 'options': options}
