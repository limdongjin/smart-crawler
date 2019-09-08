import time
from multiprocessing import Pool
from unittest import TestCase

from crawl.drivers_manager import DriversManager
from crawling_sites.likms_assembly import crawlling_moorings


class TestLikmsAssembly(TestCase):
    def test_crawling(self):
        start_time = time.time()
        res = []

        driver_manager = DriversManager()
        for i in range(0, 8):
            driver_manager.create()
        print("--- %s seconds ---" % (time.time() - start_time))

        pool = Pool(processes=8)

        for start in range(1, 100, 8):
            res.append(pool.map(crawlling_moorings, range(start, start + 8)))

            for i in range(start, start + 8):
                print("page {0} clear".format(i))
            print("--- %s seconds ---" % (time.time() - start_time))

        print("--- %s seconds ---" % (time.time() - start_time))
        print(res)

        print('delete')
        driver_manager.destroy_myself()
        pool.close()
        pool.join()

        print('end')