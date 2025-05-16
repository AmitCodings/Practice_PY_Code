class Race():
    def Problem_01(self, n=None):
        if n is None:
            print("Please provide a number.")
        elif n % 2 == 0:
            print("True")
        else:
            print("False")

object = Race()
object.Problem_01(5)  # Replace 4 with any number you want to test
