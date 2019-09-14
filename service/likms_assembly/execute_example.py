from store.dynamodb import put_items
from service.likms_assembly.main import LikmsAssemblyService
def main():
    # 의안정보시스템의 1페이지부터 30페이지까지 크롤링함.
    res = LikmsAssemblyService.moorings(1, 30)

    # dynamodb 에 결과를 저장함
    put_items('bills', res)