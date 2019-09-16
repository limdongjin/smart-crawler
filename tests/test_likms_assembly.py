from unittest import TestCase
from service.likms_assembly.main import LikmsAssemblyService
from store.dynamodb import DynamoTable


class TestLikmsAssembly(TestCase):
    def test_crawling(self):
        res = LikmsAssemblyService.moorings(1500, 1539)

        # dynamodb 에 결과를 저장함
        bills = DynamoTable('bills')
        bills.put_items(res)
