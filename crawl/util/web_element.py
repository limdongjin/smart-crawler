from typing import Dict, List, Any, Callable
from selenium.webdriver.remote.webelement import WebElement


def to_texts(_: List[WebElement]) -> List[str]:
    return list(map(lambda _: _.text, _))


def _find_head_texts(table: WebElement) -> List[str]:
    return to_texts(table.find_elements_by_tag_name('th'))


def _find_rows(table: WebElement) -> List[WebElement]:
    return table.find_elements_by_tag_name('tr')


def _find_td_texts(row: WebElement) -> List[str]:
    return to_texts(row.find_elements_by_tag_name('td'))


def _find_datas(table: WebElement) -> List[List[str]]:
    return list(map(_find_td_texts, _find_rows(table)))


def parse_table(table: WebElement) -> List[Dict[str, str]]:
    return list(map(lambda data: dict(zip(_find_head_texts(table), data)), _find_datas(table)))