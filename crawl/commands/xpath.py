from crawl.drivers_manager import DriversManager


class Xpath:
    @classmethod
    def get(cls, url: str = None, xpath: str = None):
        assert url
        assert xpath

        manager = DriversManager()
        driver = manager.create()

        driver.get(url)
        # driver.implicitly_wait(5)

        return driver.find_element_by_xpath(xpath=xpath).text
