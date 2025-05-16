# Create a class StringTools with a method is_word_palindrome
# that checks if a given word is a palindrome.

class StringTools():
    def is_word_palindrome(self, word=None):
        if word is None:
            print("Please enter a word")
        else:
            word = word.lower()  # make it case-insensitive
            reversed_word = word[::-1]
            if word == reversed_word:
                print("Palindrome")
            else:
                print("Not Palindrome")

# Create object and test
obj = StringTools()
obj.is_word_palindrome("Madam")     # ✅ Palindrome
obj.is_word_palindrome("Python")    # ❌ Not Palindrome



