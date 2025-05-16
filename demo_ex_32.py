class function_practice():
# Positional Argument
    def greet(self,name):
        print(f"Hello! {name},Good Morning!")
    def introduce(self, name, city, occupation):
        print(f"My name is {name}, i am from {city} and i am a {occupation} ")
# Keyword argument
    def person_info(self, name, age, country,profesion):
        print(f"Hello my name is {name},and i am {age} years old \n I am from {country} and i am a {profesion}")

    def greet_user(self,name,greeting="Hello"):
        print(f"{greeting}, {name}")


    def greet_multiple(*args):
        for name in args:
         print(f"Hello, {name}!")

    def add_numbers(self, *numbers):
            # TODO: Calculate the sum of all numbers in *numbers
            # Print: The sum is: <result>
            total=sum(numbers)
            print(f"The sum of number is {total}")

    def favorite_things(self, *things):
        for item in things:
            print(f"I love :{item}")


class PersonIntroduction:
    def introduce_yourself(self, **kwargs):
        print(
            f"My name is {kwargs['name']}, My age is {kwargs['age']}, I am from {kwargs['country']}, My hobby is {kwargs['hobby']}")


obj=function_practice()
# obj.greet("Amit")
# obj.introduce("Amit","Agra","\nEngineer")
# obj.person_info(name="Lalit",age= 30,profesion="Engineer",country="India")
# obj.greet_user("Lalit & Amit","Good Morning")
# obj.add_numbers(6,8,9,10)
# obj.favorite_things("Mango","Rain","Kashmir","Python")
obj.introduce_yourself("Amit,30,India,Basketball")