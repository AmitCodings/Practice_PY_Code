# Create a class NumberTools with a method is_prime(self, num) that:
# Prints "Prime" if the number is a prime number
# Otherwise prints "Not Prime"
class NumberTools():
    def is_prime(self,num=None):
        if num is None:
            print("Enter Your number ")
        elif num<=1:
            print("Not Prime")
        else:
            for i in range (2,num):
                if num % i==0:
                    print ("Not Prime")
                    break
            else:
                print ("prime")
obj=NumberTools()
obj.is_prime(45)