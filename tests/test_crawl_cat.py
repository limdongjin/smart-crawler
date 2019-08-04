import unittest
from crawl.commands.cat import DownLoader

import requests


class TestCrawlCat(unittest.TestCase):
    def test_unvalid_site_cat(self):
        with self.assertRaises(requests.RequestException):
            DownLoader("hsakln").get()

        with self.assertRaises(requests.ConnectionError):
            DownLoader("https://goo1gle.co2m").get()

        self.assertEqual(1, 1)