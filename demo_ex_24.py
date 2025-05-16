class WordCounter():
    def count_words(self,text=None):
        if text is None:
            print("Enter your text")
        else:
            original=text.strip().split()
            # print(text.count("original"))
            print(f"Word count is: {len(original)}")

obj=WordCounter()
obj.count_words("My name is Amit Mohan Sharma")