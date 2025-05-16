# while loop practice

class WhileLoopPractice():
    def print_number(self):
        i=1
        while i<=10:
            print(i)
            i+=1

    def print_even_2_to_20(self):
        i=2
        while i<=21:
            if i%2==0:
                print(i)
            i+=1

    def print_table_of_7(self):
        i=1
        while i<=10:
            print(f"7 x {i}= {7*i}")
            i+=1

    def sum_odd_1_to_50(self):
        i = 1
        total = 0
        while i <= 50:
            if i % 2 != 0:
                total += i
            i += 1
        print(f"The sum of odd numbers from 1 to 50 is {total}")

    def print_multiples_of_n_using_while(self,n=None):
        i=0
        while i<10:
            i +=1
            print(f"{n} X {i} ={i * n}")

    def print_numbers_divisible_by_3_and_5(self):
        i=1
        while i<=30:
            if i % 3 ==0 and i % 5 ==0:
                print(f"The number divisible by 3,5 are {i}")
            i +=1

    



obj=WhileLoopPractice()
obj.print_number()
obj.print_even_2_to_20()
obj.print_table_of_7()
obj.sum_odd_1_to_50()
obj.print_multiples_of_n_using_while(4)
obj.print_numbers_divisible_by_3_and_5()