# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        anagrams = []
        for test_word in word_list:
            if sorted(self.word.lower()) == sorted(test_word.lower()) and self.word.lower() != test_word.lower():
                anagrams.append(test_word)
        return anagrams