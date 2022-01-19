import boto3
from boto3.dynamodb.conditions import Key
from controller.uuid import *
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('inventory')


def post_items(payload):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    name = payload["name"]
    collection = payload["collection"]
    quantity = payload["quantity"]
    in_stock = payload["in_stock"]
    date_created = dt_string
    date_updated = dt_string
    id = str(generate_id())

    response = table.query(
        KeyConditionExpression=(Key("id").eq(id))
    )
    inventory_list = response['Items']
    if len(inventory_list) != 0:
        for item in inventory_list:
            if item["id"] == id:
                return {"message": 'Item already exists', "status_code": 406}

    table.put_item(
        Item={
            "name": name,
            "collection": collection,
            "quantity": quantity,
            "in_stock": in_stock,
            "date_created": date_created,
            "date_updated": date_updated,
            "id": str(id)
        }
    )
    return {"message": 'Item created successfully', "status_code": 201}
