class PalindromeChecker():
    def palin_checker(self,text=None):
        if text is None:
            print("Enter the text")
        else:


            if text == text[::-1]:
                print(f"The word {text} is palindrome")
            else:
                print(f"The word {text} is not palindrome")

obj=PalindromeChecker()
obj.palin_checker("madam")
obj.palin_checker("Akash")
obj.palin_checker("nurses run")