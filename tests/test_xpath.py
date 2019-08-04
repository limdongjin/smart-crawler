import unittest
from typing import Dict, List, Any, Callable

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from crawl.commands.xpath import Xpath


class TestXpath(unittest.TestCase):
    def test_get(self):
        url = "https://stackoverflow.com/questions/38727520/adding-default-parameter-value-with-type-hint-in-python"
        xpath = """//*[@id="answer-38727786"]/div/div[2]/div[1]/p[1]"""
        print(Xpath().get(url=url,
                          xpath=xpath))
        # self.fail()

        url2 = "https://newsstand.naver.com/?list=ct8&pcode=083&rndLocation=last"
        xpath2 = """//*[@id="focusPanelCenter"]/div"""

        print(Xpath().get(url=url2,
                          xpath=xpath2))

    def test_find_table(self):
        url: str = "http://likms.assembly.go.kr/bill/MooringBill.do"

        from crawl.drivers_manager import DriversManager

        driver: WebDriver = DriversManager().create()
        driver.get(url)

        tables: List[WebElement] = driver.find_elements_by_tag_name('table')
        # print(len(tables))
        # print(tables[0].get_attribute('outerHTML'))

        elements_to_texts: Callable[[Any], List[Any]] = lambda elements: list(
            map(lambda element: element.text, elements))

        th_elements: List[WebElement] = tables[0].find_elements_by_tag_name('th')

        th_texts: List[Any] = elements_to_texts(th_elements)

        print("Heads : {}".format(th_texts))
        print("Datas")

        datas: List[List[Any]] = list(map(lambda tr: elements_to_texts(tr.find_elements_by_tag_name('td')),
                                          tables[0].find_elements_by_tag_name('tr')))
        print(datas)

        final_result: List[Dict[Any, Any]] = list(map(
            lambda data: dict(zip(th_texts, data)),
            datas))

        print(final_result)
