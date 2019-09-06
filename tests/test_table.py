from unittest import TestCase
from crawl.commands.table import Table


class TestTable(TestCase):
    def test_get(self):
        url: str = "http://likms.assembly.go.kr/bill/MooringBill.do"

        print(Table.get(url))