import ipdb


class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagram_list):
        matches = []
        for word in anagram_list:
            if sorted(word) == sorted(self.word):
                matches.append(word)
        return matches


listen = Anagram("listen")
print(listen.match(['enlist', 'google', 'inlets', 'banana']))
