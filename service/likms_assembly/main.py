from crawl.drivers_manager import DriversManager
from service.likms_assembly.crawl import CrawlMooring
from util.common import flatten
from concurrent.futures import ProcessPoolExecutor, as_completed


class LikmsAssemblyService:
    @classmethod
    def moorings(cls, start_page=1, end_page=9):
        """
        usage example:
            사이트의 start_page 페이지부터 end_page 페이지까지 크롤링하고, 그에 종속된
            데이터들을 긁어옵니다.
            res = LikmsAssemblyService.moorings(1, 5)

        :param start_page:
        :param end_page:
        :return:
            ex) {'의안번호': '2022451', '의안명': '농지법 일부개정법률안(황주홍의원 등 10인)',.... }

        """
        assert start_page > 0

        driver_num = 8

        driver_manager = DriversManager()
        driver_manager.create(driver_num=driver_num)

        tasks = []
        res = []

        with ProcessPoolExecutor(max_workers=16) as executor:
            for start in range(start_page, end_page, driver_num):
                print("current page {0}".format(range(start, start + driver_num)))
                moorings = executor.map(CrawlMooring.list_page, range(start, start + driver_num))
                moorings = flatten(moorings)
                for mooring in moorings:
                    tasks.append(executor.submit(CrawlMooring.detail_page, mooring))

            for task in as_completed(tasks):
                res.append(task.result())
        print('end {0} page'.format(end_page))
        return res
