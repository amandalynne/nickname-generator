import nltk
import random
from collections import defaultdict

"""Rhyming nickname generator"""


class NicknameGenerator:
    def __init__(self):
        self.name_dict = self.create_name_dict()

    def create_name_dict(self):
        """Create a dictionary of names and pronunciations"""
        names = set(nltk.corpus.names.words())
        pron_key = nltk.corpus.cmudict.entries()
        name_dict = defaultdict(list)
        for name, pron in pron_key:
            if name in names:
                name_dict[name] = pron 
        return name_dict
        
    def gen_nickname(self, name):
        pronunciation = self.name_dict[name]


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
