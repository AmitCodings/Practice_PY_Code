               # Instance Methods and Accessing Attributes
class Person:
    # Constructor to initialize attributes
    def __init__(self, name, age, city):
        self.name = name  # Attribute 1
        self.age = age  # Attribute 2
        self.city = city  # Attribute 3

    # Instance Method 1: Display details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

    # Instance Method 2: Change the city
    def change_city(self, new_city):
        self.city = new_city
        print(f"{self.name} has moved to {self.city}.")


# Creating an object (instance) of the class
person1 = Person("Amit", 30, "Agra")

# Accessing attributes and methods
person1.display_details()
print()  # Just for a blank line

# Changing the city
person1.change_city("Delhi")

# Displaying the details again to see the change
person1.display_details()

class Laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def show_info(self):
        print(f"Name: {self.brand}")
        print(f"Age: {self.model}")
        print(f"City: {self.price}")

    def apply_discount(self):
        new_price=self.price-(self.price * 10/100)
        self.price=new_price
        print(f"The new price of laptop is {self.price}")

obj=Laptop("Acer","Aspire",50000)
obj.show_info()
obj.apply_discount()
obj.show_info()
class book:
    def __init__(self,title,auther,price):
        self.title=title
        self.auther=auther
        self.price=price

    def show_info(self):
        print(f"Title of the is book is : {self.title}")
        print(f"Auther of the book is : {self.auther}")
        print(f"The price of the book is: {self.price}")
        print()

    def apply_discount(self):
        new_price=self.price-(self.price * 10/100)
        self.price=new_price
        print(f"The new price of book is {self.price}")

obj=book("Three Idiots","Chetan Bhagat",250)
obj.show_info()
obj.apply_discount()
obj.show_info()




