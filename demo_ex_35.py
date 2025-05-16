


class DictionaryCompression():
    def dict_square_example(self):
# {key: value for item in iterable}

        square={x:x**2 for x in range (1,6)}
        print(square)

    def word_length_example(self):
        words = ["apple", "banana", "cherry"]
        length={word:len(word) for word in words}
        print(length)

    def square_of_evennumber(self):
        even_num={x:x**2 for x in range (10) if x % 2 ==0}
        print(even_num)


    def fun_exercise(self):
            even_odd = {num: "Even" if num % 2 == 0 else "Odd" for num in range(1, 11)}
            print(even_odd)

    def vowel_name_lengths(self):
        names = ["Amit", "Uday", "Raj", "Isha", "Esha", "Mohan", "Ankit"]
        hello={name:len(name) for name in names if name[0].lower() in'aeiou'}
        print(hello)




obj=DictionaryCompression()
obj.dict_square_example()
obj.word_length_example()
obj.square_of_evennumber()
obj.fun_exercise()
obj.vowel_name_lengths()
