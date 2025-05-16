# Create a class called PalindromeNumber with a method is_palindrome that
# takes a number and checks if it’s a palindrome.

class PalindromeNumer():
    def is_palindrome(self,num):
        if num is None:
            print("Enter your number")
        else:
            original=str(num)
            reversed_num=original[::-1]
            if original == reversed_num:
                print("Palindrome")
            else:
                print("Not Palindrome")

obj=PalindromeNumer()
obj.is_palindrome(1234)
obj.is_palindrome(1221)