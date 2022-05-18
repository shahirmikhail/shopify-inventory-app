from controller.get_item import *
from controller.post_item import *
from controller.delete_item import *
from controller.put_item import *


def test_put_item_success():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """

    #Post item
    payload1 = {
                "in_stock": "true",
                "name": "testing1",
                "quantity": "50",
              }
    post_items(payload1)

    #Get item
    inventory_list = get_all_items()
    item_id = 1234

    for item in inventory_list:
        if item.get("name") == "testing1":
            item_id = item.get("id")
            date_created = item.get("date_created")

    put_payload = {
        "in_stock": "true",
        "name": "testing1",
        "quantity": "29",
        "date_created": date_created,
        "id": item_id
    }

    put_item(put_payload, item_id)
    get_new_item = get_item_by_id(item_id)
    print(get_new_item)
    #Delete item
    delete_item(item_id)

    assert get_new_item.get("message")[0].get("name") == "testing1"
    assert get_new_item.get("message")[0].get("quantity") == "29"