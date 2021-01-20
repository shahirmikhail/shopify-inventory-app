class Validations:

    def __init__(self, payload=None):
        self.payload = payload
        self.error_messages = {"Validation Error": []}
        self.keys_list = payload.keys()

    def validate_payload(self):
        if 'extension' not in self.keys_list:
            error_message = {"Field": "extension", "Message": "Missing field."}
            self.error_messages["Validation Error"].append(error_message)
        if 'name' not in self.keys_list:
            error_message = {"Field": "name", "Message": "Missing field."}
            self.error_messages["Validation Error"].append(error_message)
        if 'owner' not in self.keys_list:
            error_message = {"Field": "owner", "Message": "Missing field."}
            self.error_messages["Validation Error"].append(error_message)
        if 'size' not in self.keys_list:
            error_message = {"Field": "size", "Message": "Missing field."}
            self.error_messages["Validation Error"].append(error_message)
        if 'url' not in self.keys_list:
            error_message = {"Field": "url", "Message": "Missing field."}
            self.error_messages["Validation Error"].append(error_message)

    def validate_payload_put(self):
        if 'extension' not in self.keys_list:
            error_message = {"Field": "extension", "Message": "Missing field."}
            self.error_messages["Validation Error"].append(error_message)
        if 'name' not in self.keys_list:
            error_message = {"Field": "name", "Message": "Missing field."}
            self.error_messages["Validation Error"].append(error_message)
        if 'owner' not in self.keys_list:
            error_message = {"Field": "owner", "Message": "Missing field."}
            self.error_messages["Validation Error"].append(error_message)
        if 'size' not in self.keys_list:
            error_message = {"Field": "size", "Message": "Missing field."}
            self.error_messages["Validation Error"].append(error_message)
        if 'url' not in self.keys_list:
            error_message = {"Field": "url", "Message": "Missing field."}
            self.error_messages["Validation Error"].append(error_message)
        if 'id' not in self.keys_list:
            error_message = {"Field": "id", "Message": "Missing field."}
            self.error_messages["Validation Error"].append(error_message)

    def validate(self, payload):
        extension = payload["extension"]
        name = payload["name"]
        owner = payload["owner"]
        size = payload["size"]
        url = payload["url"]

        self.validate_empty_field(extension, "extension")
        self.validate_empty_field(name, "name")
        self.validate_empty_field(owner, "owner")
        self.validate_empty_field(size, "size")
        self.validate_empty_field(url, "url")

        self.validate_string(extension, "extension")
        self.validate_string(name, "name")
        self.validate_string(owner, "owner")
        self.validate_string(size, "size")
        self.validate_string(url, "url")

        self.validate_extension(extension)
        self.validate_name(name)
        self.validate_owner(owner)
        self.validate_size(size)

    def validate_put(self, payload, uri_id):
        extension = payload["extension"]
        name = payload["name"]
        owner = payload["owner"]
        size = payload["size"]
        url = payload["url"]
        id = payload["id"]

        self.validate_empty_field(extension, "extension")
        self.validate_empty_field(name, "name")
        self.validate_empty_field(owner, "owner")
        self.validate_empty_field(size, "size")
        self.validate_empty_field(url, "url")
        self.validate_empty_field(id, "id")

        self.validate_string(extension, "extension")
        self.validate_string(name, "name")
        self.validate_string(owner, "owner")
        self.validate_string(size, "size")
        self.validate_string(url, "url")
        self.validate_string(id, "id")

        self.validate_extension(extension)
        self.validate_name(name)
        self.validate_owner(owner)
        self.validate_size(size)
        self.validate_image_id(id, uri_id)

    def validate_extension(self, extension):
        valid_extensions = ["JPEG", "JPG", "PNG", "GIF", "TIFF", "PSD", "PDF", "EPS", "AI", "INDD", "RAW"]
        if extension not in valid_extensions:
            error_message = {"Field": "extension", "Message": "Invalid extension."}
            self.error_messages["Validation Error"].append(error_message)
        return None

    def validate_name(self, name):
        self.validate_alphanumeric(name, "name")
        self.validate_string_length_min(name, "name")
        self.validate_string_length_max(name, "name")
        return None

    def validate_owner(self, owner):
        self.validate_alphanumeric(owner, "owner")
        self.validate_string_length_min(owner, "owner")
        self.validate_string_length_max(owner, "owner")
        return None

    def validate_size(self, size):
        valid_sizes = ["KB", "MB", "GB", "TB"]
        size_list = size.split(" ")
        if len(size_list) != 2:
            error_message = {"Field": "size", "Message": "Invalid format."}
            self.error_messages["Validation Error"].append(error_message)
            return None
        if (size_list[0].isnumeric() is False) or (size_list[1] not in valid_sizes):
            error_message = {"Field": "size", "Message": "Invalid format."}
            self.error_messages["Validation Error"].append(error_message)
        return None

    def validate_image_id(self, payload_id, uri_id):
        if payload_id != uri_id:
            error_message = {"Field": "id", "Message": "Id from uri does not match the one from the payload."}
            self.error_messages["Validation Error"].append(error_message)
        return None

    def validate_empty_field(self, field, field_name):
        if field == "":
            error_message = {"Field": field_name, "Message": "Empty field."}
            self.error_messages["Validation Error"].append(error_message)

    def validate_string(self, field, field_name):
        if not(type(field) == str):
            error_message = {"Field": field_name, "Message": "Field must be a string."}
            self.error_messages["Validation Error"].append(error_message)

    def validate_alphanumeric(self, field, field_name):
        is_alphanumeric = True
        string_list = field.split(" ")
        for elem in string_list:
            if elem.isalnum() is False:
                is_alphanumeric = False
        if is_alphanumeric is False:
            error_message = {"Field": field_name, "Message": "Field must be alphanumeric."}
            self.error_messages["Validation Error"].append(error_message)

    def validate_string_length_min(self, field, field_name):
        if len(field) < 5:
            error_message = {"Field": field_name, "Message": "Field must contain at least 5 characters."}
            self.error_messages["Validation Error"].append(error_message)

    def validate_string_length_max(self, field, field_name):
        if len(field) > 37:
            error_message = {"Field": field_name, "Message": "Field must contain less than 37 characters."}
            self.error_messages["Validation Error"].append(error_message)

    def validate_missing_field(self, field, field_name):
        if field not in self.keys_list:
            error_message = {"Field": field_name, "Message": "Missing field."}
            self.error_messages["Validation Error"].append(error_message)

    def get_error_messages(self):
        return self.error_messages

