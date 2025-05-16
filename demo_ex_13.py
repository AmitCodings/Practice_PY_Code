# Create a method that takes a string input and
# returns the number of uppercase and lowercase characters separately.

class StringTools():
    def count_case(self, text=None):
        if text is None:
            print("Please enter a string.")
        else:
            upper_count = 0
            lower_count = 0

            for char in text:
                if char.isupper():
                    upper_count += 1
                elif char.islower():
                    lower_count += 1

            print("Uppercase letters:", upper_count)
            print("Lowercase letters:", lower_count)


# Object creation and method call
obj = StringTools()
obj.count_case("HeLLo TeSTinG")
