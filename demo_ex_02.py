class Maths():
    def is_positive(self,n=None):
        if n is None:
            print("Please provide a number :- ")
        elif n>0:
            print("Positive")

        else:
            print("Negative")

object=Maths()
object.is_positive(-5)

