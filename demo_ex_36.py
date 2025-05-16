class map_filter():
    def mapping(self):
        numbers = [1, 2, 3, 4, 5]
        square=list(map(lambda x:x**2,numbers))
        print(square)


    def filter(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        even_number=list(filter(lambda x:x % 2==0,numbers))
        odd_number=list(filter(lambda x:x % 2!=0 ,numbers))
        print(even_number)
        print(odd_number)


    def practice(self):
        numbers = [1, 2, 3, 4, 5, 6]
        even = list(map(lambda x: x % 2 == 0, numbers))
        print(even)  # Output: [2, 4, 6]
        numbers = [1, 2, 3, 4, 5, 6]
        even = list(filter(lambda x: x % 2 == 0, numbers))
        print(even)  # Output: [2, 4, 6]





obj=map_filter()
# obj.mapping()
# obj.filter()
obj.practice()