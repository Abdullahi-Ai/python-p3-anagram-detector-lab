# your code goes here!
class Anagram:
    def __init__(self, word):  
        self.word = word

    def match(self, possible_anagrams):
        normalized_word = sorted(self.word.lower())  
        matches = []

        for candidate in possible_anagrams:
            if sorted(candidate.lower()) == normalized_word:
                matches.append(candidate)

        return matches



anagram_checker = Anagram('listen')
possible_anagrams = ['enlists', 'google', 'inlets', 'banana']
print(anagram_checker.match(possible_anagrams))  