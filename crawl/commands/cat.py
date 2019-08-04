from crawl.http.downloader import DownLoader
from crawl.drivers_manager import DriversManager


class Cat:

    @classmethod
    def with_simple(cls, site_name):
        return DownLoader(site_name).get()


    @classmethod
    def with_selenium(cls, site_name):
        manager = DriversManager()

        driver = manager.create()
        result = DownLoader(site_name, selenium=True, driver=driver).get()
        return result
