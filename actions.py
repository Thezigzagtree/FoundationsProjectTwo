# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "ZigZagVille"


def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!\n=======================" % site_name)


def print_stores():
    print("CURRENT SHOP LIST: ")
    for store in stores:
        print(store.name)


def valid_store(store_name):
    for store in stores:
        if (store_name.capitalize() == store.name):
            return True

    return False


def get_store(store_name):
    for store in stores:
        if (store_name.capitalize() == store.name):
            return store


def pick_store(cart):
    print_stores()
    selection = input(
        "Pick a store by typing its name. Or type 'checkout' to pay your bills and say your goodbyes.\n================\n")
    if (selection.lower() == "checkout"):
        cart.checkout()
    elif (valid_store(selection)):

        pick_products(cart, get_store(selection))
        print("================")
        cart.printItems()
    else:
        print("Please choose a valid store to shop at")
        cart.printItems()

    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!


def pick_products(cart, picked_store):
    while cart.checkedOut == False:
        cart.printItems()
        picked_store.print_products()
        storeSelect = input("Which item would you like to purchase?\n")
        if (storeSelect.lower() == "checkout"):
            cart.checkout()
        elif(picked_store.checkProduct(storeSelect)):
            cart.add_to_cart(
                picked_store.getProduct(storeSelect))
        elif (storeSelect.lower() == "exit" or storeSelect.lower() == "back"):
            return
        else:
            print("Please select a valid product")

    """
    prints list of products and prompts user to add products to card.
    """


def shop():
    cart = Cart()
    while cart.checkedOut == False:
        pick_store(cart)
    """
    The main shopping functionality
    """

    # your code goes here!


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
    exit()
