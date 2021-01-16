import boto3
from boto3.dynamodb.conditions import Key
from controller.uuid import *

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('images')


def post_images(payload):
    name = payload["name"]
    extension = payload["extension"]
    url = payload["url"]
    size = payload["size"]
    owner = payload["owner"]
    id = str(generate_id())

    response = table.query(
        KeyConditionExpression=(Key("id").eq(id))
    )
    image_list = response['Items']
    if len(image_list) != 0:
        for image in image_list:
            if image["id"] == id:
                return {"message": 'Image already exists', "status_code": 406}

    table.put_item(
        Item={
            "name": name,
            "extension": extension,
            "url": url,
            "size": size,
            "owner": owner,
            "id": str(id)
        }
    )
    return {"message": 'Image created successfully', "status_code": 201}
