class ErrorHandlingExamples:
    def safe_division(self, a, b):
        try:
            result = a / b
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Oops! Division by zero is not allowed.")
        finally:
            print("Division attempt finished.")

    def convert_to_int(self,value):
        # value="Amir"
        try:
            result = int(value)  # This might raise ValueError
            print(f"Converted value: {result}")
        except ValueError:
            print("Oops! That’s not a valid number!")
        finally:
            print("Conversion attempt finished.")



obj=ErrorHandlingExamples()
# obj.safe_division(10,2)
# obj.safe_division(23,0)
# obj.convert_to_int("Amit")
# obj.convert_to_int(825.756)
obj.convert_to_int(-45)
obj.convert_to_int(45.89)
obj.convert_to_int("abc")
obj.convert_to_int("3455")
obj.convert_to_int("345sdc")
obj.convert_to_int("12.89")