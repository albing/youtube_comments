import random
from collections import defaultdict

class Predictor():


    class Word():
        def __init__(self, input_dict=None):
            self.next = defaultdict(int)
            if not input_dict:
                self.count = 1
            else:
                self.count = input_dict['count']
                self.next.update(input_dict['next'])


        def add(self, word):
            self.next[word] += 1


    def __init__(self, input_dict=None):
        self.words = {}
        self.last_word = ''

        if input_dict:
            for word, word_info in input_dict.items():
                self.words[word] = self.Word(word_info)


    def add(self, word:str):
        if word not in self.words:
            self.words[word] = self.Word()
        else:
            self.words[word].count += 1
            self.words[word].next

        if self.last_word:
            self.words[self.last_word].add(word)
        self.last_word = word


    def terminate(self):
        self.words[self.last_word].add('.')
        self.last_word = ''


    def dict(self):
        return {
            word: {'count': word_obj.count, 'next': dict(word_obj.next)}
            for word, word_obj in self.words.items()
        }

    def random_walk_step(self, word):
        #word_obj = self.words[word]
        #total_count = word_obj.count
        choices = self.words[word].next.keys()
        return random.choice(list(choices))


