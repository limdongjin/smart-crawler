from service.likms_assembly.main import LikmsAssemblyService
from store.dynamodb import DynamoTable

def main():
    # 의안정보시스템의 1페이지부터 1000페이지까지 크롤링함.
    res = LikmsAssemblyService.moorings(1, 1000)

    # dynamodb 에 결과를 저장함
    bills = DynamoTable('bills')
    bills.put_items(res)
