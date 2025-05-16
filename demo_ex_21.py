class InitialsExtractor():
    def Extractor(self,text=None):
        if text is None:
            print("Enter your text")
        else:
            parts= text.strip().split()
            initials = ".".join([name[0].upper() for name in parts])
            print(f"your initial are {initials}")

obj=InitialsExtractor()
obj.Extractor("Jai Bajrang Bali")