import time
import logging
from selenium.common.exceptions import JavascriptException, TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ConnectAndExecuteScript:
    driver: WebDriver

    def __init__(self, driver):
        self.driver = driver

    def run(self, url, script=None, max_repeat=1, wait_element=None):
        for i in range(max_repeat):
            try:
                self.driver.get(url)
                if script is not None:
                    self.driver.execute_script(script)

                if wait_element is not None:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, wait_element))
                    )
                break
            except JavascriptException:
                if i == 3:
                    logging.info('fail!1 {0}'.format(script))
                    return None
                time.sleep(8)
            except IndexError:
                if i == 3:
                    print('fail! {0}'.format(script))
                    return None
                time.sleep(8)
            except TimeoutException:
                if i == 3:
                    print('fail! {0}'.format(script))
                    return None
                time.sleep(8)
        return self.driver.page_source
