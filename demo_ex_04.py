# Create a class NumberCheck with a method is_multiple_of_five(self, num)
# Print "Yes" if the number is a multiple of 5
# Otherwise, print "No"
class NumberCheck():
    def is_multiple_of_five(self,n=None):
        if n is None:
            print("Enter your Number:-")
        elif n%5==0:
            print("Yes")
        else:
            print("NO")

obj=NumberCheck()
obj.is_multiple_of_five(25)










