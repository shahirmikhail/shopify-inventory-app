import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('images')


def put_image(payload, image_id):
    name = payload["name"]
    extension = payload["extension"]
    url = payload["url"]
    size = payload["size"]
    owner = payload["owner"]

    response = table.scan(**{'FilterExpression': Key('id').eq(image_id)})
    image_list = response['Items']

    if len(image_list) != 0:
        table.delete_item(
            Key={
                "id": image_id,
            }
        )
        table.put_item(
            Item={
                "name": name,
                "extension": extension,
                "url": url,
                "size": size,
                "owner": owner,
                "id": image_id
            }
        )
        return {"message": 'Image updated successfully', "status_code": 200}
    elif len(image_list) == 0:
        return {"message": 'Image not found.', "status_code": 404}
