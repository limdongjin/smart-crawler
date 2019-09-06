
from bs4 import BeautifulSoup
from bs4.element import Tag
from crawl.util.common import to_texts
from typing import Callable, List, Dict, Any


def parse_tables(source: str):
    soup: BeautifulSoup = BeautifulSoup(source, features='html.parser')
    tables: Tag = soup.find_all('table')

    return list(map(lambda _: parse_table(_), tables))


def parse_table(table_element: Tag) -> List[Dict[Any, Any]]:
    read_ths: Callable[[Tag], Tag] = lambda table: table.find_all('th')
    read_rows: Callable[[Tag], List[Tag]] = (
        lambda table: list(map(
            lambda tr: tr.find_all('td'), table.find_all('tr')
        )))

    find_a_from_row: Callable[[Tag], List[Dict[str, str]]] = (
        lambda row: list(map(
            lambda a: a.attrs,
            filter(lambda _: _ is not None, map(lambda td: td.a, row))
        ))
    )
    read_links = lambda table: list(map(find_a_from_row, read_rows(table)))
    to_strips = lambda its: map(lambda it: it.strip(), filter(lambda _: type(_) is str, its))

    _parse_table: Callable[[Tag], List[Dict[str, str]]] = (
        lambda table: (
            list(map(lambda row:
                     dict(zip(
                         to_strips(to_texts(read_ths(table))), to_strips(to_texts(row))
                     )), read_rows(table))
                 )))

    parsed_table = _parse_table(table_element)
    links: List[Dict[str, List[Any]]] = list(map(lambda _: {'links': list(_)}, read_links(table_element)))
    parsed_table = list(map(lambda row, link: dict(row, **link), parsed_table, links))

    return parsed_table
