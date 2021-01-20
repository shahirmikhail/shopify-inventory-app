import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('images')


def delete_image(image_id):
    response = table.scan(**{'FilterExpression': Key('id').eq(image_id)})
    image_list = response['Items']
    if len(image_list) != 0:
        table.delete_item(
            Key={
                "id": image_id
            }
        )
        return {"message": 'Image deleted successfully', "status_code": 200}
    else:
        return {"message": 'Image not found.', "status_code": 404}
