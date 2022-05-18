from controller.get_item import *
from controller.post_item import *
from controller.delete_item import *

def test_delete_item_success():
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

    inventory_list_new = get_all_items()
    flag = True
    for item in inventory_list_new:
        if item.get("name") == "testing1" or item.get("name") == "testing2":
            flag = False


    assert count == 2
    assert flag == True