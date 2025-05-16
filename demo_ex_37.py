class car():
    # Constructor method to initialize the attributes
    def __init__(self,brand,model,year):
        self.brand = brand #Attribute
        self.model = model #Attribute
        self.year =  year  #Attribute

    # Method to display information about the car
    def start_engine(self):
        print(f"{self.brand},{self.model},{self.year} is strating")

# Creating objects
car1=car("Toyota","Fortuner","2021")
car2=car("maruti","Wagnor","2023")

# Accessing attributes and calling methods on objects
print(car1.brand)
car1.start_engine()

print(car2.brand)
car2.start_engine()




