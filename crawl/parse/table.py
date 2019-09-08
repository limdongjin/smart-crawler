
from bs4 import BeautifulSoup
from bs4.element import Tag
from crawl.util.common import to_texts
from typing import Callable, List, Dict, Any


def parse_tables(source: str):
    soup: BeautifulSoup = BeautifulSoup(source, features='html.parser')
    tables: Tag = soup.find_all('table')

    return list(map(lambda _: _parse_table(_), tables))


def _parse_table(table_element: Tag) -> dict:
    """

    :param table_element: Tag
    :return: {'tag_name': 'table', 'attrs': {}, 'rows': [{.., 'links': []},{..},]}


    find_x_all: Callable[[str], Callable[[Tag], List[Tag]]] = lambda x: lambda from_: from_.find_all(x)
    read_ths_from = find_x_all('th')
    read_trs_from = find_x_all('tr')
    read_tds_from = find_x_all('td')

    read_rows: Callable[[Tag], List[List[Tag]]] = (
        lambda table: list(filter(is_not_equal_empty_list, map(
            lambda tr: read_tds_from(tr), read_trs_from(table)
        ))))

    find_a_from_row: Callable[[Tag], List[Dict[str, str]]] = (
        lambda row: list(map(
            lambda a: a.attrs,
            filter(is_not_none, map(lambda td: td.a, row))
        ))
    )

    read_links = lambda table: list(map(find_a_from_row, read_rows(table)))
    to_strips = lambda its: map(lambda it: it.strip(), filter(lambda _: type(_) is str, its))

    _parse_table_rows_data: Callable[[Tag], List[Dict[str, str]]] = (
        lambda table: (
            list(map(lambda row:
                     dict(zip(
                         to_strips(to_texts(read_ths_from(table))), to_strips(to_texts(row))
                     )), read_rows(table))
                 )))

    parsed_table_rows_data = _parse_table_rows_data(table_element)
    links: List[Dict[str, List[Any]]] = list(map(lambda _: {'links': list(_)}, read_links(table_element)))
    parsed_table_rows_data = merge_list_dict(parsed_table_rows_data, links)

    return parsed_table
