class FunnyNameMaker():
    def reverse_name_order(self, text=None):
        if text is None:
            print("Enter your text")
        else:
            parts =text.strip().split()
            reversed_part= parts[::-1]
            funny_name=" ".join(reversed_part)
            print(f"Your funny name is :{funny_name}")

obj=FunnyNameMaker()
obj.reverse_name_order("Amit Mohan Sharma")
obj.reverse_name_order("Ecyclopideia")
