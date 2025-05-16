# Create a class called ReverseNumber with a method reverse_num
# that takes a number and prints its reverse

class ReverseNumber():
    def reverse_num(self,num=None ):
        if num is None:
            print("Enter you number")
        else:
            reversed_num = str(num)[::-1]
            print(reversed_num)

obj=ReverseNumber()
obj.reverse_num(1357)
