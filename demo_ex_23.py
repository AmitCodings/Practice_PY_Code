class WordReplacer():
    def replace_word(self,sentence=None,old_word=None,new_word=None):
        if None in (sentence,new_word,old_word):
            print("provide your sentence,word to replace,and new word")
        else:
            updated=sentence.replace(old_word,new_word)
            print(f"your updated sentence is {updated}")

obj=WordReplacer()
obj.replace_word("I love Python Programming","Python","Java")
