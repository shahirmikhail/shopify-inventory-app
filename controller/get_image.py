import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('images')


def get_all_images():
    response = table.scan()
    image_list = response['Items']
    return image_list


def get_image_by_id(image_id):
    response = table.scan(**{'FilterExpression': Key('id').eq(image_id)})
    image_list = response['Items']
    if len(image_list) != 0:
        return {"message": image_list, "status_code": 200}
    else:
        return {"message": "Image not found.", "status_code": 404}

