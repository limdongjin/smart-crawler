import unittest
from crawl.commands.xpath import Xpath


class TestXpath(unittest.TestCase):
    def test_get(self):
        url = "https://stackoverflow.com/questions/38727520/adding-default-parameter-value-with-type-hint-in-python"
        xpath = """//*[@id="answer-38727786"]/div/div[2]/div[1]/p[1]"""
        print(Xpath().get(url=url,
                          xpath=xpath))
        # self.fail()
