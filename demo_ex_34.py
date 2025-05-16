# List and dictionary comprehension
class Squares_of_numbers():
    def exersise_01(self):
     # squares = [x ** 2 for x in range(1, 6)]
        # print(squares)  # Output: [1, 4, 9, 16, 25]
        squares=[x ** 2 for x in range(1,11) if x % 2==0 ]
        print(squares)

    def exersise_02(self):
        words = ["apple", "banana", "apricot", "cherry", "avocado"]
        new_words = [x for x in words if x[0].lower() == "a"]
        print("Words starting with 'a':", new_words)


    def exersise_03(self):
        num=[x for x in range(1,51) if x % 5==0 and x % 3==0]
        print(num)



obj=Squares_of_numbers()
obj.exersise_01()
obj.exersise_02()
obj.exersise_03()
