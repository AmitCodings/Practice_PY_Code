# Write a method that takes a user’s name and age, and prints:
class UserInfoPrinter():
    def user(self):
        name="Amit"
        age=29

        print(f"My name is {name} and my age is {age}")

obj=UserInfoPrinter()
obj.user()

class ProductTagGenerator():
    def price_tag(self,price=None):
        if price is None:
            print("Enter Your Price")
        else :
            print(f"The price of iphone is {price}")

obj=ProductTagGenerator()
obj.price_tag("122222")

class MathReporter():
    def addition(self):
        a=55
        b=54
        print(f"The sum of a & b is {a+b}")

obj=MathReporter()
obj.addition()

class ReverseSentenceFormatter():
    def formatter(self,sentence=None):
        if sentence is None:
            print("Enter the text")
        else:
            # txt = "Hello World"[::-1]
            print(f"Original text is {sentence} and the reverse of text is {sentence[::-1]}")

obj=ReverseSentenceFormatter()
obj.formatter("Doctor")

class InitialsExtractor():
    def get_initials(self, full_name=None):
        if full_name is None:
            print("Please enter your full name")
        else:
            parts = full_name.strip().split()  # ["Amit", "Mohan", "Sharma"]
            initials = ".".join([name[0].upper() for name in parts])  # A.M.S
            print(f"Your initials are: {initials}")

obj = InitialsExtractor()
obj.get_initials("Amit Mohan Sharma")
