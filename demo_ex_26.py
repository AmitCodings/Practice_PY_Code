# Class Name: WordLengthReporter
# Objective: Print the length of each word in the sentence.

class WordLengthReporter():
    def length_reporter(self,text=None):
        if text is None:
            print("Enter your text ")

        else:
            original = text.strip().split()
            for word in original:
                print(f"The word '{word}' has {len(word)} characters.")

obj=WordLengthReporter()
obj.length_reporter("Taj Mahal")