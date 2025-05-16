# For loop practice

class ForLoopPractice():
    def print_number_1_to_5(self):
        for i in range (1,5):
            print(i)


    def odd_number(self):
        for i in range(1,20):
            if i%2!=0:
                print(i)


    def table_of_5(self):
        for i in range(1,11):
            print(f"5 X {i}={5*i}")

    def sum_even_1_to_50(self):
        total=0
        for i in range (1,51):
            if i%2==0:
                total += i
        print(f"The sum of all even no between 1 to 50 is {total}")

    def print_divisible_by_3(self):

        for i in range (1,31):
            if i % 3==0:
                print(i)

    def print_multiples_of_n(self,n=None):
        if n is None:
            print("Enter your number:-")

        else:
            for i in range(1,11):
                print(f"{n} x {i}={n*i}")

    def print_squares_1_to_10(self):
        for i in range(1,11):
            # print(f"{i} ^ {2} = ",i * i)
            print(f"{i} ^ 2 = {i * i}")


obj=ForLoopPractice()
obj.odd_number()
obj.print_number_1_to_5()
obj.table_of_5()
obj.sum_even_1_to_50()
obj.print_divisible_by_3()
obj.print_multiples_of_n(8)
obj.print_squares_1_to_10()