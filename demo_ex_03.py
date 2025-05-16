# Create a class EvenOdd with a method check(self, num) that prints:
#
# "Even" if the number is even
#
# "Odd" if the number is odd

class EvenOdd():
    def Even_Odd_function(self,num=None):
        if num is None:
            print ("Please provide a number ")

        elif num%2==0:
            print("Even")
        else:
            print("Odd")

Obj=EvenOdd()
Obj.Even_Odd_function(63)