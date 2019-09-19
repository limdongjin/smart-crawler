import lxml.etree
import lxml.html
from parse import ParseTargetIsEmpty
from util.common import to_strings, is_all_elements_type


def parse_by_xpath(source: str, xpath: str):

    html = lxml.html.fromstring(source)

    type(html)

    res = html.xpath(xpath)
    # ".../text()" 같은 형식의 text 를 뽑는 xpath 의 type 은 List<lxml.etree._ElementUnicodeResult>
    # text() 외의 나머지 경우에는 List<lxml.html.HtmlElement>

    # if type(res) is lxml.etree._ElementUnicodeResult:
    #     return str(res)
    if is_all_elements_type(res, lxml.etree._ElementUnicodeResult):
        return to_strings(res)

    # 못 찾을시에는 res 는 비어있는 리스트 이므로 예외 발생 시킴
    try:
        res = res[0]
    except IndexError:
        raise ParseTargetIsEmpty

    # HtmlElement 타입은 str 로 변환해서 리턴해야함
    return lxml.etree.tostring(res).decode()
