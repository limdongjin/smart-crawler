import time
from multiprocessing import Pool

from crawl.drivers_manager import DriversManager
# from crawling_sites.likms_assembly.crawl import crawl_list_page, crawl_detail_and_merge
from crawling_sites.likms_assembly.crawl import Crawl
from util.common import flatten


class LikmsAssembly:
    @classmethod
    def moorings(cls, start_page=1, end_page=9):
        assert start_page > 0

        driver_num = process_num = 8

        driver_manager = DriversManager()
        driver_manager.create(driver_num=driver_num)

        start_time = time.time()
        moorings = []

        print("--- %s seconds ---" % (time.time() - start_time))
        with Pool(processes=process_num) as pool:
            for start in range(start_page, end_page, driver_num):
                moorings.extend(pool.map(Crawl.list_page, range(start, start + process_num)))
                print("{0} pages success".format(tuple(range(start, start + 8))))
                print("--- %s seconds ---" % (time.time() - start_time))

        print("--- %s seconds ---" % (time.time() - start_time))
        moorings = flatten(moorings)
        print(moorings)
        with Pool(processes=16) as pool:
            res = pool.map(Crawl.detail_page, moorings)

        # res = flatten(res)
        print(res)
        print("--- %s seconds ---" % (time.time() - start_time))

        return res
