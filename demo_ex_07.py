# Create a class NumberTools with a method is_armstrong(self, num)
# Check if a number is an Armstrong number.

class NumberTools():
    def is_armstrong(self,num=None):
        if num is None:
            print("Enter your Number ")
        else:
            num_str = str(num)
            num_digits = len(num_str)
            total=0

            for digit in num_str:
                total += int(digit) ** num_digits

            if total == num:
                print("Armstrong Number")
            else:
                print("Not Armstrong Number")

obj = NumberTools()
obj.is_armstrong(153)
obj.is_armstrong(123)




