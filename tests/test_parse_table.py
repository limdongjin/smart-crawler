# -*- coding: utf-8 -*-

from unittest import TestCase
from crawl.commands.table import Table
from crawl.parse.table import parse_tables
from crawl.parse.xpath import parse_by_xpath
from crawl.drivers_manager import DriversManager
from util.common import to_strips
from bs4 import BeautifulSoup

url: str = "http://likms.assembly.go.kr/bill/MooringBill.do"


class TestTable(TestCase):
    def test_table_crawling(self):
        print(Table.get(url))

    def test_table_crawling_and_detail_page(self):
        res = Table.get(url)

        table0 = res[0]
        # print(table0)
        # table0 = list(filter(lambda dic: list(dic.values()) != [[]], table0))
        print(table0['attrs']['summary'])
        print(table0['rows'])

        driver = DriversManager().create()

        # driver.get(url)
        # driver.execute_script(table0[0]['links'][0]['href'])

        detail_page2 = 'http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_T1O6F0C6T2N8A1O7I3I6Z3J2J8R9K5'
        driver.get(detail_page2)

        page_source = driver.page_source
        soup = BeautifulSoup(page_source)

        # 심사 진행 단계
        soup.find_all('span', class_='on')

        # tables[0] : 의안 접수 정보 테이블
        # tables[1] : 위원회 접수 테이블
        # ... tables[x]['attrs']['summary'] 로 테이블 이름 확인 가능
        # ... tables[x]['rows'] 로 데이터 접근
        # tables[-1] : X
        tables = parse_tables(page_source)
        print(tables)

        # 제안이유 및 주요내용
        # ['제안이유', 'bla', 'bla']
        summaries = list(filter(lambda _: _,
                                to_strips(parse_by_xpath(page_source,
                                                         '//*[@id="summaryContentDiv"]/text()'))))
        print(summaries)
