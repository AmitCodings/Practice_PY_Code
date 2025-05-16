# Count how many times each vowel appears in a given string

class VowelFrequencyChecker():
    def count_vowel_frequency(self, text=None):
        if text is None:
            print ("Enter your text")
        else:
            vowels=["a","e","i","o","u"]
            text=text.lower()
            for vowel in vowels:
                print(f"{vowel}: {text.count(vowel)}")


obj=VowelFrequencyChecker()
obj.count_vowel_frequency("My name is Amit Mohan Sharma")