from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from config_handler.reader import ConfigReader
from util.singleton import Singleton
import logging


class DriversManager(metaclass=Singleton):
    drivers: List[WebDriver]
    chrome_options: Options

    def __init__(self):
        self.drivers = []
        self.chrome_options = webdriver.ChromeOptions()

        self._configure_options()

    def __del__(self):
        for driver in self.drivers:
            logging.debug('del {0}'.format(driver))
            driver.quit()

    def create(self, driver_num=1) -> WebDriver:
        driver = None
        try:
            for i in range(0, driver_num):
                driver = webdriver.Chrome(executable_path=self.executable_path,
                                          options=self.chrome_options)
                self.drivers.append(driver)
            return driver
        except WebDriverException as e:
            print(e)
            print("Check your chromedriver path or re install.")
            assert False

    def count(self):
        return len(self.drivers)

    def _configure_options(self):
        conf: dict = ConfigReader.get("selenium")

        if conf['headless']:
            self.chrome_options.add_argument('--headless')
            self.chrome_options.add_argument('--no-sandbox')
            self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.add_argument("disable-gpu")
        self.executable_path = conf['chrome_driver_binary']

        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 1,
                                                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                            'notifications': 2, 'auto_select_certificate': 2,
                                                            'fullscreen': 2,
                                                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                            'media_stream_mic': 2, 'media_stream_camera': 2,
                                                            'protocol_handlers': 2,
                                                            'ppapi_broker': 2, 'automatic_downloads': 2,
                                                            'midi_sysex': 2,
                                                            'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                            'metro_switch_to_   desktop': 2,
                                                            'protected_media_identifier': 2, 'app_banner': 2,
                                                            'site_engagement': 2,
                                                            'durable_storage': 2}}
        self.chrome_options.add_experimental_option('prefs', prefs)
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_argument("disable-infobars")
        self.chrome_options.add_argument("--disable-extensions")