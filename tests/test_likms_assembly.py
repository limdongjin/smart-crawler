import time
from multiprocessing import Pool
from unittest import TestCase

from crawl.drivers_manager import DriversManager
from crawling_sites.likms_assembly.crawl import crawlling_moorings
from util.common import flatten


class TestLikmsAssembly(TestCase):
    def test_crawling(self):
        start_time = time.time()
        res = []

        driver_manager = DriversManager()
        for i in range(0, 8):
            driver_manager.create()
        print("--- %s seconds ---" % (time.time() - start_time))

        process_num = 8
        pool = Pool(processes=process_num)

        for start in range(1, 10, process_num):
            res.extend(pool.map(crawlling_moorings, range(start, start + process_num)))
            for i in range(start, start + 8):
                print("page {0} clear".format(i))
            print("--- %s seconds ---" % (time.time() - start_time))

        print("--- %s seconds ---" % (time.time() - start_time))

        res = flatten(res)
        print(res)

        driver_manager.destroy_myself()
        pool.close()
        pool.join()