import boto3


class DynamoTable:
    def __init__(self, table_name):
        self._resource_dynamodb = boto3.resource('dynamodb')
        self._table = self._resource_dynamodb.Table(table_name)
        self.items = None

    def get_all_items(self, cached=True):
        if cached is True and self.items is not None:
            return self.items

        res = self._table.scan()
        data = res['Items']
        while 'LastEvaluatedKey' in res:
            res = self._table.scan(ExclusiveStartKey=res['LastEvaluatedKey'])
            data.extend(res['Items'])

        self.items = data
        return data

    def put(self, item):
        return self._table.put_item(Item=item)

    def put_items(self, items):
        with self._table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item)

        return True
