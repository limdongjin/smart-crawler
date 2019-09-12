from unittest import TestCase

from crawling_sites.likms_assembly.main import LikmsAssembly


class TestLikmsAssembly(TestCase):
    def test_crawling(self):
        res = LikmsAssembly.moorings(1, 100)

        print('res!')
        print(res)