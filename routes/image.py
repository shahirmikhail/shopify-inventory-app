from app import app
from flask import jsonify, request, make_response
from controller.get_image import *
from controller.post_image import *
from api_exceptions import *
from controller.validations import Validations

"""
Image API
    - GET: returns all images in the DB
        - if successful, status code: 200 (OK)
        - if no images are found, returns and empty payload, status code: 404 (NOT FOUND)
        
    - POST: creates and adds image to the DB, generates image ID
        - if successful, status code: 201 (CREATED)
        - if information in payload is missing, status code: 406 (NOT ACCEPTABLE)
        - if image already exists in DB, status code: 406 (NOT ACCEPTABLE)
        - if schema error, return 400 (BAD REQUEST)
        
    - PUT: modifies an image in the DB given an image ID
        - if successful, status code: 200 (OK)
        - if image not found, status code: 404 (NOT FOUND)
        - if information in payload is missing, status code: 406 (NOT ACCEPTABLE)
        - if schema error, return 400 (BAD REQUEST)
        
    - DELETE: deletes an image from the DB given an image ID
        - if successful, status code: 200 (OK)
        - if image not found, status code: 404 (NOT FOUND)
"""


@app.route('/api/images', methods=['POST', 'GET'])
def image_api():
    if request.method == 'GET':
        images = get_all_images()
        response = make_response(jsonify(images), 200)
        return response

    if request.method == 'POST':
        data = request.get_json()
        try:
            validation = Validations(data)

            validation.validate_payload()
            error_messages = validation.get_error_messages()
            if not(len(error_messages["Validation Error"]) == 0):
                return jsonify({'message': validation.error_messages}), 406

            validation.validate(data)
            error_messages = validation.get_error_messages()
            if not(len(error_messages["Validation Error"]) == 0):
                return jsonify({'message': validation.error_messages}), 406

            response = post_images(data)
            if response['status_code'] == 201:
                return jsonify({
                    'message': response['message']
                }), response['status_code']
            elif response['status_code'] == 400:
                return jsonify({'message': response['message']}), 400
            elif response['status_code'] == 406:
                return jsonify({'message': response['message']}), 406
        except ApiException as e:
            return jsonify({'message': str(e)}), 406


@app.route('/api/images/<image_id>', methods=['GET', 'PUT', 'DELETE'])
def image_id_api(image_id):
    if request.method == 'GET':
        response = get_image_by_id(image_id)
        if response['status_code'] == 200:
            return jsonify(response['message']), response['status_code']
        else:
            return jsonify({'message': response['message']}), 400

    if request.method == 'PUT':
        data = request.get_json()
        return None

    if request.method == 'DELETE':
        return None


@app.route('/api/test/images', methods=['GET'])
def test_image_api():
    return jsonify({'message': 'Image API is up and running.'}), 200
