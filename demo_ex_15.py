# Challenge: Count consonants in a string
class StringAnalyzer():
    def count_consonants(self,text=None):
        if text is None:
            print("Enter your text")
        else :
            vowels=["a","e","i","o","u"]
            count=0
            for char in text.lower():
                if char.isalpha() and char not in vowels:
                    count += 1

            print("Consonants:", count)

obj=StringAnalyzer()
obj.count_consonants("Amit Sharma")