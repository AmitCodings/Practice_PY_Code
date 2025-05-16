class StringChecker():
    def count_uppercase(self, text=None):
        if text is None:
            print("Please enter some text")
        else:
            count = 0
            for char in text:
                if char.isupper():
                    count += 1
            print("Uppercase letters:", count)

obj = StringChecker()
obj.count_uppercase("MyNameIsAmit")
