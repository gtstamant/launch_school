"""
Problem:
Take a word and a list of candidate words
Return list of candidates that are anagrams of word

Data Structure:
A list to store the candidate anagram matches

Algorithm:
We could maybe just use regex here. Can I build
programatically?

n times
[word][word][word]

actually can do this much more easily without regex

"""
print('testing')

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        return [word for word in list
                if sorted(word.casefold()) == sorted(self.word.casefold())
                if word.casefold() != self.word.casefold()]

    # def _get_regex(self):
    #     return fr'[{self.word}]' * len(self.word)

    # def match(self, list):
    #     regex = self._get_regex()
    #     return [word for word in list
    #             if re.match(regex, word, flags=re.I)
    #             if word.casefold() != self.word.casefold()
    #             if sorted(word.casefold()) == sorted(self.word.casefold())]