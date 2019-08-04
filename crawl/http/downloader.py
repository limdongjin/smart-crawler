import requests


class DownLoader:
    def __init__(self, site_name, selenium=False, driver=None):
        self.site_name = site_name
        self.selenium = selenium
        self.driver = driver

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
        self.driver.get(self.site_name)
        page_source = self.driver.page_source

        return page_source
