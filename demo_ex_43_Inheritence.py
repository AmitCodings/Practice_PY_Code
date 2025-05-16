# Simple Inheritance — Basic parent-child inheritance.
#
# Method Overriding — Rewriting parent class methods in the child class.
#
# super() Function — Accessing parent class methods and attributes.
#
# Multiple Inheritance — Inheriting from multiple parent classes.
#
# Multilevel Inheritance — Inheritance chain of multiple classes.
class Animal:
    def __init__(self,species):
        self.species=species

    def make_sound(self):
        print("Some random sound")

class Cat(Animal):
    def Meow(self):
        print(f"Meow,Meow")

Cat1=Cat("Desi")

Cat1.make_sound()
Cat1.Meow()

#-------------------Simple Inheritence--------------------

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age= age

    def show_info(self):
        print(f"Name :- {self.name}")
        print(f"Age :- {self.age}")

class Employee(Person):
    def __init__ (self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary

        # Overriding the show_info() method
    def show_info(self):
        super().show_info()
        print(f"The salary of the Employee is {self.salary}")



Emp1=Employee("Amit",30,45000)

Emp1.show_info()

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def show_info(self):
        print(f"Name:-{self.name}")
        print(f"Price:-{self.price}")

class Electronics(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name,price)
        self.warranty_period=warranty_period

    def show_info(self):
        super().show_info()
        print(f"The warranty period of {self.name} is {self.warranty_period}")


obj=Electronics("Fan",1500,5)
obj.show_info()

#---------------------Multiple Inheritance-------------------------

class Parent1:
    def parent1_method(self):
        print("This is parent 1 method")

class Parent2:
    def parent2_method(self):
        print("This Parent 2 method")

class Child(Parent1,Parent2):
    def child_method(self):
        print("This is child method")

obj=Child()
obj.parent1_method()
obj.parent2_method()
obj.child_method()



class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_person_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

class Job:
    def __init__(self,designation,salary):
        self.designation=designation
        self.salary =salary

    def show_job_info(self):
        print(f"Designation :- {self.designation}")
        print(f"Salary :-{self.salary}")

class Employee(Person,Job):
    def __init__(self,name,age,designation,salary):
        # Call the constructors of both parent classes

        Person.__init__(self,name,age)
        Job.__init__(self,designation,salary)

    def show_info(self):

        print(f"These are the full details of the Employee")
        self.show_person_info()
        self.show_job_info()

obj=Employee("Amit",30,"Engineer",50000)
obj.show_person_info()
obj.show_job_info()
obj.show_info()


class Device:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def show_device_info(self):
        print(f"Brand :-{self.brand}")
        print(f"Model :-{self.model}")

class Network:
    def __init__(self,carrier,data_plan):
        self.carrier=carrier
        self.data_plan=data_plan

    def show_network_info(self):
        print(f"Carrier :-{self.carrier}")
        print(f"Data Plan :-{self.data_plan}")

class Smartphone(Device,Network):
    def __init__(self,brand,model,carrier,data_plan):
# Call the constructor of the parent class
        Device.__init__(self,brand,model)
        Network.__init__(self,carrier,data_plan)

    def show_info(self):
        print("Please find the full details below")
        Smartphone.show_device_info()
        Smartphone.show_network_info()

obj=Smartphone("Realme","GT 6T","Airtel",[349])
obj.show_device_info()
obj.show_network_info()

class Hardware:
    def __init__(self,processor,RAM,storage):
        self.processor=processor
        self.RAM=RAM
        self.storage=storage

    def show_HW_info(self):
        print(f"Processor : {self.processor}")
        print(f"RAM : {self.RAM}")
        print(f"storage : {self.storage}")

class Software:
    def __init__(self,Operating_System,Installed_Application):
        self.Operating_System=Operating_System
        self.Installed_Application=Installed_Application

    def show_Software_info(self):
        print(f"Operating System : {self.Operating_System}")
        print(f"Installed_application : {self.Installed_Application}")

class Laptop(Hardware,Software):
    def __init__(self,processor,RAM,storage,Operating_System,Installed_Application):

        Hardware.__init__(self,processor,RAM,storage)
        Software.__init__(self,Operating_System,Installed_Application)


    def show_info(self):

        print("Please find the below details")
        self.show_HW_info()
        self.show_Software_info()

obj=Laptop("Mediatek",16,256,"Windows","Facebook",)
obj.show_info()



