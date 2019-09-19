from unittest import TestCase
from parse import parse_by_xpath
from tests.fake_data.html.lxml_de import source as lxml_source
from tests.fake_data.html.python_org import source as python_org_source


class TestParseByXpath(TestCase):
    def test_parse_by_xpath(self):
        answer = ['lxml - XML and HTML with Python']
        xpath = '//*[@id="lxml"]/h1/text()'
        assert answer == parse_by_xpath(lxml_source, xpath)

    def test_python_org_parse(self):
        answer = '<span class="linkdescr" style="user-select: auto;">all functions, classes, terms</span>'
        xpath = '/html/body/div[2]/div[1]/div/div/table[2]/tbody/tr/td[1]/p[2]/span'

        assert answer == parse_by_xpath(python_org_source, xpath)
