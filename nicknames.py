import nltk
import random
from collections import defaultdict

"""Rhyming nickname generator"""

class NicknameGenerator:
    def __init__(self):
        self._names = set(nltk.corpus.names.words())
        self._pron_key = nltk.corpus.cmudict.entries()
        
        self.name_dict = self.create_name_dict()
        self.nouns_dict = self.create_nouns_dict()

    def create_name_dict(self):
        """Create a dictionary of names and pronunciations"""
        name_dict = defaultdict(list)
        for name, pron in self._pron_key:
            if name.title() in self._names:
                name_dict[name] = pron 
        return name_dict
            
    def create_nouns_dict(self):
        nouns_dict = defaultdict(list)
        for name, pron in self._pron_key:
            if name.title() not in self._names and nltk.pos_tag([word])=='NN':
                nouns_dict[name] = pron
        return nouns_dict

    def syllable_count(self, phones):
        syllables = 0
        pass

    def gen_nickname(self, name):
        pronunciation = self.name_dict[name]
        candidates = []
        for word, pron in self.nouns_dict.items():
            pass  
    


def main():
    ng = NicknameGenerator()
    
    while True: 
        name = raw_input("Enter a name: ")
        nickname = ng.gen_nickname(name)
        print("Your nickname is {}".format(nickname))
        again = raw_input("Go again? ")
        if again.lower() in ['no','n']:
            break 

if __name__ == "__main__":
    main()
