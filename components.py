# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def print_products(self):
        for item in self.products:
            print(item)

    def checkProduct(self, inq):
        for product in self.products:
            if (inq.lower() == product.name.lower()):
                return True
        return False

    def getProduct(self, inq):
        for product in self.products:
            if (inq.lower() == product.name.lower()):
                return product


class Product():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return("%s" % self.name)


class Cart():
    def __init__(self):
        self.products = []
        self.checkedOut = False

    def add_to_cart(self, product):
        self.products.append(product)

    def get_total_price(self):
        total = 0
        for item in self.products:
            total += item.price
        return total

    def print_receipt(self):
        print("You Want:")
        for product in self.products:
            print("- %s" % product.name)
        print("=======================")
        print("Total price is : %s" % self.get_total_price())

    def checkout(self):
        self.print_receipt()
        finalChoice = input("Do you want to complete this purchase? (Type Yes or Y to Confirm) : ")
        if (finalChoice.lower() == "yes" or finalChoice.lower() == "y"):
            self.products = []
            self.checkedOut = True
            print ("Your purchase has been completed!")
        else:
            print ("You may continue to shop")

        


        """
        Does the checkout.
        """

    def printItems(self):
        if (not self.checkedOut == True and len(self.products) > 0):
            print("=======================")
            print("YOUR CART IS : ")
            for product in self.products:
                print(product.name)
            print("=======================")
