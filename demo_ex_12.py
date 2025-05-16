# Create a class DigitTools with a method count_digits that
# takes a number and prints how many digits it has.
class DigitalTools():
    def count_digit(self,num=None):
        if num is None:
            print ("Enter your Number")
        else:
            original=len(str(num))
            print(original)


obj=DigitalTools()
obj.count_digit(3456)



