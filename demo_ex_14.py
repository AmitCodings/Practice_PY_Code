# Question: Count the number of words in a string

class StringCounter():
    def count_word(self,text=None):
        if text is None:
            print("Enter your Text")
        else:
            text=str(text)
            words=text.split()
            print("Total words:",len(words))

obj=StringCounter()
obj.count_word("Bahat mata ki jai")
# obj.count_word("12345 5666")