# Class Variables vs. Instance Variables

class Book:
    # Class Variable (Shared across all instances)
    category = "Fiction"

    def __init__(self, title, author, price):
        # Instance Variables (Unique for each instance)
        self.title = title
        self.author = author
        self.price = price

    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")# Creating objects
        print(f"Category: {self.category}")


book1 = Book("1984", "George Orwell", 300)
book2 = Book("Brave New World", "Aldous Huxley", 350)

book1.show_info()
print()
book2.show_info()


class Employee:
    company_name="Saffo Tech"

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def display_info(self):
        print(f"My name is :- {self.name}")
        print(f"I am {self.age} years old")
        print(f"my salary is :- {self.salary}")
        print(f"My company name is {self.company_name}")
        print()

    def apply_increment(self):
        new_salary=self.salary + (self.salary * 10/100)
        self.salary=new_salary
        print(f"My incremented salary is {self.salary}")

obj=Employee("Amit Mohan Sharma",30,40000)
obj.display_info()
obj.apply_increment()
obj.display_info()



class Student:
    school_name="Delhi Public School"
    def __init__(self,names,grade,marks):
        self.name=names
        self.grade=grade
        self.marks=marks

    def show_details(self):
        print(f"My name is :- {self.name}")
        print(f"My grade is :- {self.grade}")
        print(f"My marks are :- {self.marks}")
        print(f"My school name is :- {Student.school_name}")
        print()

    def cal_average(self):
        average = sum(self.marks) / len(self.marks)
        self.marks=average
        print(f"The average of marks is :- {self.marks}")
        print()




student1=Student("Amit",12,[78,89,77,76,86])
student2=Student("Lalit",12,[77,88,95,65,78])
student1.show_details()
student1.cal_average()
student2.show_details()
student2.cal_average()



