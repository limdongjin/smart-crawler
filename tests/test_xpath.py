import unittest
from typing import Dict, List, Any, Callable

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from crawl.drivers_manager import DriversManager

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
        pass