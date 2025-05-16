class StringAnalyzer2():
    def count_spaces(self, text=None):
        if text is None:
            print("Please enter some text")
        else:
            count = 0
            for char in text:
                if  char.isspace():
                    count += 1
            print("Space Count:", count)


obj = StringAnalyzer2()
obj.count_spaces("My name is Amit Sharma")
