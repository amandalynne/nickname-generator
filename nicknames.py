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
        self._vowels = set(['A','E','I','O','U'])
        
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
        """Create dictionary of nouns and pronunciations"""
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
  
 
    def syllable_count(self, phones):
        syllables = 0
        for phone in phones:
            print phone
            if phone[-1].isdigit():
                syllables+=1
        return syllables

    def rhyme(self, phones):
        rhyme_part = []
        vowels = 0
        for phone in reversed(phones):
            rhyme_part.append(phone)
            if vowels == 1:
                break
            if phone[0] in self._vowels:
                vowels+=1
        rhyme_part.reverse()
        return rhyme_part 
    
 
    def last_two_syllables(self, phones):
        syllables = []
        vowels = 0 
        for phone in reversed(phones):
            if vowels > 1: 
                break 
            if phone[0] in self._vowels:
                vowels+=1
            syllables.append(phone)
        syllables.reverse()
        return syllable

    def gen_nickname(self, name):
        if name not in self._names:
            return "Sorry, I don't know how to pronounce your name."
        pronunciation = self.name_dict[name.title()]
        candidates = []
        if self.syllable_count(pronunciation) == 1:
            rhyme_part = self.rhyme(pronunciation)
        else:
            rhyme_part = self.last_two_syllables(pronunciation)
        for word, pron in self.nouns_dict.items():
            
        return  
         

