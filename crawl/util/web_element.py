
from typing import Dict, List, Callable
from selenium.webdriver.remote.webelement import WebElement

from crawl.util.common import to_texts


def _parse_ths(table: WebElement) -> List[str]:
    return to_texts(table.find_elements_by_tag_name('th'))


def _parse_tds(table: WebElement) -> List[List[str]]:
    _find_td_texts: Callable[[WebElement], List[str]] = (
        lambda _: to_texts(_.find_elements_by_tag_name('td'))
    )
    _find_rows: Callable[[WebElement], List[WebElement]] = (
        lambda _: _.find_elements_by_tag_name('tr')
    )
    return list(map(_find_td_texts, _find_rows(table)))


def parse_table(table: WebElement) -> List[Dict[str, str]]:
    return list(map(lambda data: dict(zip(_parse_ths(table), data)), _parse_tds(table)))
