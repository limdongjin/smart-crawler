
from crawl.parse.table import parse_tables
from crawl.drivers_manager import DriversManager
from util.common import merge_dict, to_strips
from crawl.parse.xpath import parse_by_xpath
from selenium.common.exceptions import JavascriptException
from bs4 import BeautifulSoup
import re
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

    for mooring in moorings:
        mooring['prc'] = _get_prc_xxx(mooring)
        mooring['url'] = 'http://likms.assembly.go.kr/bill/billDetail.do?billId=' + mooring['prc']

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

    res['proponents'] = _crawl_proponents(driver, url)

    return res


# 법안 발의자
def _crawl_proponents(driver, detail_url: str):
    url = 'http://likms.assembly.go.kr/bill/coactorListPopup.do?billId='+_get_prc_xxx(detail_url)
    driver.get(url)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source)

    soup = soup.find('div', class_='links textType02 mt20')
    a_tags = soup.find_all('a')

    proponents = []
    for a in a_tags:
        proponent = dict()

        proponent['url'] = a.attrs['href']

        # ex) a.text = '이장우(새누리당/李莊雨)'
        (proponent['한글이름'],
         proponent['정당'],
         proponent['한자이름']) = tuple(re.split('[(:/:)]', a.text)[:-1])
        proponent['유형'] = '공동발의자'

        proponents.append(proponent)

    bill_title = parse_by_xpath(page_source, '//*[@id="periodDiv"]/div[2]/p/text()')[0]

    # ex)  '[2022357]2018년도 산업통상자원... 감사요구안(산업통상자원중소벤처기업위원장)'
    # ex2) [2022392]선박직원법 일부개정법률안(황주홍의원 등 13인)
    main_proponent = re.split('[(:)]', bill_title)[-2]
    if main_proponent.find('의원 등'):
        main_proponent = main_proponent.split('의원 등')[0]
        for proponent in proponents:
            if proponent['한글이름'] == main_proponent:
                proponent['유형'] = '대표발의자'
    else:
        proponents.append({'한글이름': main_proponent,
                           '정당': '',
                           '한자이름': '',
                           '유형': main_proponent})

    return proponents


def _get_prc_xxx(mooring):
    if type(mooring) is str:
        return mooring.split('billId=')[1]
    return mooring['links'][0]['href'].split("'")[1]
