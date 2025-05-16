# Create a method is_perfect(self, num) that:
# Prints "Perfect Number" if it’s perfect
# Otherwise prints "Not Perfect Number"

class PerfectNumber():
    def is_perfect(self,num=None):
        if num is None:
            print ("Enter your Number")
        else:
            total=0
            for i in range (1,num):
                if num%i==0:
                    total+=i
            if total==num:
                print("Perfect")
            else:
                print("Not Perfect")

obj=PerfectNumber()
obj.is_perfect(6)





