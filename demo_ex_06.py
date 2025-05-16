# Create a class called NumberTools with a method is_palindrome(self, num)
# It should:
# Print "Palindrome" if the number is a palindrome
# Print "Not Palindrome" if it's not

class NumberTools():
    def is_palindrome(self, num=None):
        if num is None:
            print("Please enter a number")
        else:
            original = str(num)
            reversed_num = original[::-1]

            if original == reversed_num:
                print("Palindrome")
            else:
                print("Not Palindrome")


obj = NumberTools()
obj.is_palindrome(121)  # Output: Palindrome
obj.is_palindrome(123)  # Output: Not Palindrome

