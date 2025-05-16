class Person:
    def __init__(self,name,age):
        self.name= name
        self.age =age

    def show_info(self):
        print(f"Name:{self.name}")
        print(f"Age :{self.age}")

class Employee(Person):
    def __init__(self,name,age,salary):
    # Call the parent constructor
     super().__init__(name,age)
    # Adding additional attribute specific to Employee
     self.salary=salary

    # Overriding the show_info() method
    def show_info(self):
        super().show_info() # Call the parent method to show name and age
        print(f"Salary of the Employee is {self.salary}")

obj=Employee("Amit",30,50000)
obj.show_info()
