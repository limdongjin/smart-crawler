import time

from selenium.common.exceptions import JavascriptException


class ConnectAndExecuteScript:
    def __init__(self, driver):
        self.driver = driver

    def run(self, url, script=None, max_repeat=1):
        for i in range(max_repeat):
            try:
                self.driver.get(url)
                if script is not None:
                    self.driver.execute_script(script)
                if i > 0:
                    print('success')
                break
            except JavascriptException:
                if i == 3:
                    print('fail!')
                    return None
                print('re-try connect. n={0}'.format(i))
                time.sleep(5)
            except IndexError:
                if i == 3:
                    print('fail!')
                    return None
                print('re-try connect. n={0}'.format(i))
                time.sleep(5)
        return self.driver.page_source