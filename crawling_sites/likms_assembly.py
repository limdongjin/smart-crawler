
from crawl.parse.table import parse_tables
from crawl.drivers_manager import DriversManager
from util.common import merge_dict, to_strips
from crawl.parse.xpath import parse_by_xpath
from selenium.common.exceptions import JavascriptException
from bs4 import BeautifulSoup
import time


def crawlling_moorings(page=1):

    driver = DriversManager().drivers[page % 8]

    moorings_base_url: str = "http://likms.assembly.go.kr/bill/MooringBill.do"
    moorings = []

    for i in range(4):
        try:
            if i > 0:
                print("re-try connect page={0}, n={1}".format(page, i))
            driver.get(moorings_base_url)
            if page != 1:
                driver.execute_script("javascript:GoPage({0})".format(page))
            if i > 0:
                print('success')
            page_source = driver.page_source

            moorings = parse_tables(page_source)
            moorings = moorings[0]['rows']

            break
        except JavascriptException:
            if i == 3:
                print('fail')
                return []
            time.sleep(5)
        except IndexError:
            if i == 3:
                print('fail')
                return []
            time.sleep(5)

    get_PRC_XXX = lambda mooring: mooring['links'][0]['href'].split("'")[1]

    for mooring in moorings:
        mooring['url'] = 'http://likms.assembly.go.kr/bill/billDetail.do?billId=' + get_PRC_XXX(mooring)

    res = list(map(lambda _: merge_dict(_, _crawl_bill(driver, _['url'])), moorings))

    return res


def _crawl_bill(driver, url: str):
    res = {}
    driver.get(url)

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, features='html.parser')

    # 심사 진행 단계
    res['status'] = soup.find('span', class_='on').text
    # print(res['status'].text)

    tables = parse_tables(page_source)
    # tables[0] : 의안 접수 정보 테이블
    # tables[1] : 위원회 접수 테이블
    # ... tables[x]['attrs']['summary'] 로 테이블 이름 확인 가능
    # ... tables[x]['rows'] 로 데이터 접근

    valid_info = lambda _: _['attrs'] != {} and _['attrs']['summary'] != '등록의견 리스트의 번호, 제목, 작성자, 의견제출기관, 등록일 정보'
    res['informationTables'] = list(filter(valid_info, tables))
    # res['informationTables'] = tables
    # print(res)

    # 제안이유 및 주요내용
    # ['제안이유', 'bla', 'bla']
    summaries = list(filter(lambda _: _,
                            to_strips(parse_by_xpath(page_source,
                                                     '//*[@id="summaryContentDiv"]/text()'))))
    res['summaries'] = summaries

    return res
