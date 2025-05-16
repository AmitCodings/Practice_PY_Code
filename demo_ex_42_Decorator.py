class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self._speed=speed

    @property

    def speed(self):
        return self._speed

    @speed.setter

    def speed(self,value):
        if value >=0:
            self._speed=value

        else:
            print(f"The speed cannot be negative!.")

#Creating object
Car1=Car("Maruti",200)

#Accesing attribute using property decorator
print(Car1.speed)


#Setting Value
Car1.speed=230
#

class Student:
    def __init__(self,name,marks):
        self.name=name
        self._marks=marks

    @property
    def average(self):

        return sum(self._marks)/len(self._marks)

    @average.setter
    def average(self,value):
        print(f"The average cannot be set directly")
#Creating Instance
Student1=Student("Amit",[86,87,98,88,80])

#Getting Average
print(Student1.average)

#Setting Average
Student1.average= 58








