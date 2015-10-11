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
        
        self.names_dict = self.create_names_dict()
        self.nouns_dict = self.create_nouns_dict()
        self.verbs_dict = self.create_verbs_dict()
        self.adjs_dict = self.create_adjs_dict()


    def create_names_dict(self):
        """Create a dictionary of names and pronunciations"""
        if os.path.isfile('names.json'):
            with open('names.json','rb') as inf:
                names_dict = json.load(inf)
        else:
            names_dict = defaultdict(list)
            for name, pron in self._pron_key:
                if name.title() in self._names:
                    names_dict[name.title()] = pron
            with open('names.json', 'wb') as outf:
                json.dump(names_dict, outf)
        return names_dict

            
    def create_nouns_dict(self):
        """Create dictionary of nouns and pronunciations"""
        if os.path.isfile('nouns.json'):
            with open('nouns.json','rb') as inf:
                nouns_dict = json.load(inf)
        else:
            nouns_dict = defaultdict(list)
            for word, pron in self._pron_key:
                pos_tag = nltk.pos_tag([word])[0][1]
                if (word.title() not in self._names and pos_tag == 'NN'):
                    nouns_dict[word] = pron
            with open('nouns.json','wb') as outf:
                json.dump(nouns_dict, outf)  
        return nouns_dict


    def create_verbs_dict(self):
        """Create dictionary of gerunds and pronunciations,
           but change pronunciation for better "rhyme" """
        if os.path.isfile('verbs.json'):
            with open('verbs.json','rb') as inf:
                verbs_dict = json.load(inf)
        else:
            verbs_dict = defaultdict(list)
            for word, pron in self._pron_key:
                pos_tag = nltk.pos_tag([word])[0][1]
                if (word.title() not in self._names and pos_tag == 'VBG'):
                    pron[-1] = 'N'
                    verbs_dict[word] = pron
            with open('verbs.json','wb') as outf:
                json.dump(verbs_dict, outf)  
        return verbs_dict


    def create_adjs_dict(self):
        """Create dictionary of adjectives and pronunciations"""
        if os.path.isfile('adjs.json'):
            with open('adjs.json','rb') as inf:
                adjs_dict = json.load(inf)
        else:
            adjs_dict = defaultdict(list)
            for word, pron in self._pron_key:
                # Is there a way to not run this 133K times
                test_sent = "I am {}".format(word).split()
                pos_tag = nltk.pos_tag(test_sent)[2][1]
                if (word.title() not in self._names and pos_tag == 'JJ'):
                    adjs_dict[word] = pron
            with open('adjs.json','wb') as outf:
                json.dump(adjs_dict, outf)  
        return adjs_dict
 
    def syllable_count(self, phones):
        syllables = 0
        for phone in phones:
            if phone[-1].isdigit():
                syllables+=1
        return syllables


    def rhyme(self, phones):
        rhyme_part = []
        vowels = 0
        syllables = self.syllable_count(phones)
        if syllables == 1: 
            for phone in reversed(phones):
                if vowels == 1:
                    break
                rhyme_part.append(phone)
                if phone[0] in self._vowels:
                    vowels+=1
        else:
            for phone in reversed(phones):
                if vowels > 1: 
                    break 
                if phone[0] in self._vowels:
                    vowels+=1
                rhyme_part.append(phone)
        rhyme_part.reverse()
        return rhyme_part 
    
    def gen_nickname(self, pos, name):
        """
        Pass a POS as well to choose from adj, verb, or noun
        nickname
        """
        name = name.title()
        if name not in self._names:
            return None 
        pronunciation = self.names_dict[name]
        candidates = []
        name_rhyme_part = self.rhyme(pronunciation)
            
        

        for word, pron in d.items():
            word_rhyme_part = self.rhyme(pron)
            if name_rhyme_part == word_rhyme_part:
                candidates.append(word)           
        if not candidates:
            return None
        return random.choice(candidates).title()
         

