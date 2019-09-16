import re
from bs4 import BeautifulSoup
import logging
from crawl.connect_and_execute_script import ConnectAndExecuteScript
from crawl.parse.table import parse_tables
from crawl.drivers_manager import DriversManager
from util.common import merge_dict, to_strips
from crawl.parse.xpath import parse_by_xpath
from crawl.connect import Connect

logging.basicConfig(level=logging.INFO)


class CrawlMooring:
    @classmethod
    def detail_page(cls, mooring):
        return merge_dict(mooring, _CrawlBills.detail_page(mooring['url']))

    @classmethod
    def list_page(cls, page):
        return _CrawlBills(page, 'mooring').list_page()


class _CrawlBills:
    def __init__(self, page, category):
        self.page = page
        self.driver = DriversManager().drivers[page % 8]
        self.category = category
        self.url = "http://likms.assembly.go.kr/bill/MooringBill.do" if category == 'mooring' else None

    def list_page(self):
        script = 'javascript:GoPage({0})'.format(self.page) if self.page != 1 else None
        page_source = ConnectAndExecuteScript(self.driver).run(url=self.url,
                                                               script=script,
                                                               max_repeat=8,
                                                               wait_element='table')

        try:
            moorings = parse_tables(page_source)[0]['rows']
        except IndexError as e:
            logging.info(e)
            logging.info(page_source)
            logging.info(('page = {0}'.format(self.page)))
            return []

        for mooring in moorings:
            mooring['prc'] = self._get_prc_xxx(mooring)
            mooring['url'] = 'http://likms.assembly.go.kr/bill/billDetail.do?billId=' + mooring['prc']
            mooring['id'] = int(mooring['의안번호'])

        for mooring in moorings:
            for key in mooring:
                if mooring[key] == '':
                    mooring[key] = None

        return moorings

    @classmethod
    def detail_page(cls, url):
        res = {}
        page_source = Connect.request(url, max_repeat=4)
        # page_source = requests.get(url).text

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

        res['proponents'] = cls._crawl_proponents(url)

        tmp = parse_by_xpath(page_source, '/html/body/div[1]/div[2]/div[2]/div/div[7]/div/text()')
        res['비고'] = tmp[0] if tmp else None

        logging.debug(res)
        return res

    @classmethod
    def _crawl_proponents(cls, detail_url: str):
        url = 'http://likms.assembly.go.kr/bill/coactorListPopup.do?billId=' + cls._get_prc_xxx(detail_url)

        page_source = Connect.request(url, max_repeat=4)

        soup = BeautifulSoup(page_source, features='html.parser')

        soup = soup.find('div', class_='links textType02 mt20')
        a_tags = soup.find_all('a')

        proponents = []
        for a_tag in a_tags:
            proponent = dict()

            proponent['url'] = a_tag.attrs['href'] if 'href' in a_tag.attrs else None
            try:
                # ex) a_tag.text = '이장우(새누리당/李莊雨)'
                tup = tuple(re.split('[(:/:)]', a_tag.text)[:-1])
                proponent['한글이름'] = tup[0]
                proponent['정당'] = tup[1]
                proponent['한자이름'] = tup[-1]
            except ValueError:
                print(a_tag.text)
                (proponent['한글이름'],
                 proponent['정당'],
                 proponent['한자이름']) = (None, None, None)
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
                               '정당': None,
                               '한자이름': None,
                               '유형': main_proponent})
        logging.debug(proponents)
        return proponents

    @classmethod
    def _get_prc_xxx(cls, mooring):
        if isinstance(mooring, str):
            return mooring.split('billId=')[1]
        return mooring['links'][0]['href'].split("'")[1]
