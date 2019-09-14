from bs4 import BeautifulSoup
from bs4.element import Tag
from util.common import (to_texts,
                         is_not_none,
                         to_strips,
                         merge_list_dict,
                         is_not_equal_empty_list,
                         flatten)
from typing import Callable, List, Dict, Any
from functional import seq
import logging

# [TODO] tag wrapper class 만들기 및 크롤링 되는 대상에 대한 wrapper
# [TODO] 기능 좀더 추상화


def parse_tables(source: str):
    soup: BeautifulSoup = BeautifulSoup(source, features='html.parser')
    tables: Tag = soup.find_all('table')

    return list(map(lambda _: _parse_table(_), tables))


def _parse_table(table_element: Tag) -> dict:
    """

    :param table_element: Tag
    :return: {'tag_name': 'table', 'attrs': {}, 'rows': [{.., 'links': []},{..},]}

    return example 1)
    {
        'tag_name': 'table',
        'attrs': {'summary': 'my table'},
        'rows': [
            {
                'th1': 'dat',
                'links': [{'href': 'http://google.com'}]
            },
            {},..
        ]
    }
    """
    assert type(table_element) == Tag

    read_rows = (lambda table: seq(table.find_all('tr'))
                 .map(lambda tr: tr.find_all('td'))
                 .filter(is_not_equal_empty_list))

    # find_a_from_row = (lambda row: seq(row)
    #                    .map(lambda td: td.find_all('a'))
    #                    .filter(is_not_equal_empty_list))

    read_links = (lambda table: seq(read_rows(table))
                  .map(find_a_from_row))

    ths_text = lambda table: seq(table.find_all('th')).map(lambda _: _.text.strip())

    _parse_table_rows_data = (lambda table: seq(read_rows(table))
                      .map(to_texts)
                      .map(to_strips)
                      .map(lambda row: dict(zip(ths_text(table), row))))
    parsed_table_rows_data = _parse_table_rows_data(table_element)
    links: List[Dict[str, List[Any]]] = (seq(read_links(table_element))
                                         .map(lambda _: {'links': list(_)}))
    print(links)
    parsed_table_rows_data = merge_list_dict(parsed_table_rows_data, links)

    res = {'tag_name': 'table', 'attrs': table_element.attrs, 'rows': parsed_table_rows_data}

    for row in res['rows']:
        for key in row:
            if row[key] == '':
                row[key] = None

    logging.debug(res)

    return res


def find_a_from_row(row):

    a_tags = (seq(row)
        .map(lambda td: td.find_all('a'))
        .filter(is_not_equal_empty_list))
    return list(seq(flatten(a_tags)).map(lambda a: a.attrs))