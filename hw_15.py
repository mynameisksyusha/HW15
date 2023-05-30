# Practice

# Task 1.
# Create a class Product with properties name, price, and quantity.
# Create a child class Book that inherits from Product and adds a property author and a method called read.

class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):

    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"You are reading a book {self.name} written by {self.author}.")


book = Book("'Harry Potter'", "300$", "1", "J.R.")
book.read()


# Task 2.

# Create a class Restaurant with properties name, cuisine, and menu.
# The menu property should be a dictionary with keys being the dish name and values being the price.
# Create a child class FastFood that inherits from Restaurant and adds a property drive_thru (a boolean indicating whether the restaurant has a drive-thru or not)
# and a method called order which takes in the dish name and quantity and returns the total cost of the order.
# The method should also update the menu dictionary to subtract the ordered quantity from the available quantity.
# If the dish is not available or if the requested quantity is greater than the available quantity, the method should return a message indicating that the order cannot be fulfilled.

class Restaurant:

    def __init__(self):
        self.name = "U_Ksyushi"
        self.cuisine = "Ukrainian"

        self.menu = {
            "buckwheat": {
                "price": 40,
                "quantity": 20
            },
            "borscht": {
                "price": 80,
                "quantity": 17
            },
            "salo": {
                "price": 40,
                "quantity": 15
            },
            "bread": {
                "price": 20,
                "quantity": 43
            },
            "varenyky": {
                "price": 120,
                "quantity": 18
            },
            "sour cream": {
                "price": 30,
                "quantity": 17
            }}


class FastFood(Restaurant):

    def __init__(self, drive_thru):
        super().__init__()
        self.drive_thru = drive_thru

    def order(self, dish, quantity):
        ordered_dish = self.menu[dish]
        if ordered_dish == None:
            print(f"Dish {dish} is not in our menu.")
        else:
            if ordered_dish["quantity"] - quantity >= 0:
                ordered_dish["quantity"] -= quantity
                total_cost = quantity * ordered_dish["price"]
                print(total_cost)
            else:
                print("The order cannot be fulfilled. Not enough dishes.")


fast_food = FastFood(True)

fast_food.order("bread", 42)
fast_food.order("salo", 1)
