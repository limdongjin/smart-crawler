from unittest import TestCase

from service.likms_assembly.main import LikmsAssemblyService
from store.dynamodb import put_items


class TestLikmsAssembly(TestCase):
    def test_crawling(self):
        res = LikmsAssemblyService.moorings(1, 1000)

        # dynamodb 에 결과를 저장함
        put_items('bills', res)