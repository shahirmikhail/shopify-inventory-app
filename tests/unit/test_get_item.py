from controller.get_item import *
from controller.post_item import *
from controller.delete_item import *

def test_get_all_items_success():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """

    #Post items
    payload1 = {
                "in_stock": "true",
                "name": "testing1",
                "quantity": "50",
              }
    payload2 = {
        "in_stock": "true",
        "name": "testing2",
        "quantity": "50",
    }
    post_items(payload1)
    post_items(payload2)

    #Get items
    inventory_list = get_all_items()

    #Delete items
    count = 0
    for item in inventory_list:
        if item.get("name") == "testing1" or item.get("name") == "testing2":
            count = count + 1
            item_id = item.get("id")
            delete_item(item_id)

    assert count == 2


def test_get_item_by_id_success():
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

    get_item = get_item_by_id(item_id)

    #Delete item
    delete_item(item_id)

    assert get_item.get("message")[0].get("name") == "testing1"
    assert get_item.get("message")[0].get("id") is not None


def test_get_item_by_collection_success():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """

    #Post items
    payload1 = {
                "collection": "testing_collection",
                "in_stock": "true",
                "name": "testing1",
                "quantity": "50",
              }
    payload2 = {
        "collection": "testing_collection",
        "in_stock": "true",
        "name": "testing2",
        "quantity": "50",
    }
    post_items(payload1)
    post_items(payload2)

    #Get items
    all_items = get_all_items()
    collection_items = get_item_by_collection("testing_collection")

    #Delete items
    count = 0
    for item in all_items:
        if item.get("name") == "testing1" or item.get("name") == "testing2":
            count = count + 1
            item_id = item.get("id")
            delete_item(item_id)

    assert count == 2
    assert collection_items.get("message")[0].get("collection") == "testing_collection"
    assert collection_items.get("message")[1].get("collection") == "testing_collection"