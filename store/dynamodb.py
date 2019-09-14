import boto3


def get_dynamodb():
    return boto3.resource('dynamodb')


def get_table(table_name):
    dynamodb = get_dynamodb()
    return dynamodb.Table(table_name)


def put(table_name, item, table=None):
    if not table:
        table = get_table(table_name)
    return table.put_item(Item=item)


def put_items(table_name, items, table=None):
    if not table:
        table = get_table(table_name=table_name)
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)

    return True
