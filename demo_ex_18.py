# Count the number of digits in a given string.

class StringDigitCounter():
    def count_digits(self, text=None):
        if text is None:
            print("Enter your text")
        else:
            count=0
            for char in text:
                if char.isdigit():
                    count += 1
            print("Count of digit:-", count)

obj=StringDigitCounter()
obj.count_digits("My name is Amit 420")