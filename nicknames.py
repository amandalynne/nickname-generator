import json
import nltk
import os
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
                name_dict[name.title()] = pron 
        return name_dict
            
    def create_nouns_dict(self):
        if os.path.isfile('nouns.json'):
            with open('nouns.json','rb') as inf:
                nouns_dict = json.load(inf)
        else:
            nouns_dict = defaultdict(list)
            for word, pron in self._pron_key:
                if (word.title() not in self._names
                        and nltk.pos_tag([word])=='NN'):
                    nouns_dict[word] = pron
            with open('nouns.json','wb') as outf:
                json.dump(nouns_dict, outf)  
        return nouns_dict
   
    # TO DO: pickle nouns; maybe sonority hierarchy? 

    def syllable_count(self, phones):
        syllables = 0
        for phone in phones:
            print phone
            if phone[-1].isdigit():
                syllables+=1
        return syllables
        
    def last_syllable(self, phones):
        syllable = []
        for phone in reversed(phones):
            pass     
        return syllable

    def gen_nickname(self, name):
        pronunciation = self.name_dict[name.title()]
        candidates = []
        #for word, pron in self.nouns_dict.items():
        return self.syllable_count(pronunciation)   
         

