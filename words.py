import wonderwords
from wonderwords import RandomSentence, RandomWord
import random
import os
import re


def create_sentence(length):
    text = []
    for i in range(0,length):
        s = RandomSentence()
        text.append(s.sentence())
    
    return text

 
def easy_word():
    w = RandomWord()
    r = RandomSentence()
    text = [r.word(word_max_length=4) for _ in range(300)]
    return text

def medium_word():
    text = []
    for i in range(0,25):
        s = RandomSentence()
        w = RandomWord()
        text.append(w.word(word_min_length=7, word_max_length=11))

    return text

def hard_word():
    text = []
    for i in range(0,20):
        s = RandomSentence()
        w = RandomWord()
        text.append(w.word(word_min_length=14))
    return text

def read_words_from_file(file_path):
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            cleaned_words = [re.sub(r'[^a-zA-Z]', '', word).lower() for word in line.split()]
            cleaned_words = list(filter(None, cleaned_words))
            if cleaned_words:
                words.append(cleaned_words)
    return words

def easy_words():
    easy_words_path = 'easyWords.txt' 

    if os.path.exists(easy_words_path):
        with open(easy_words_path, 'r') as file:
            easy_words = [line.strip() for line in file]
        
        random.shuffle(easy_words)
    
        selected_words = easy_words[:300]
        return selected_words
    else:
        w = RandomWord()
        return [w.word(word_max_length=4) for _ in range(300)]

def medium_words():
    medium_words_path = 'mediumWords.txt' 

    if os.path.exists(medium_words_path):
        with open(medium_words_path, 'r') as file:
            easy_words = [line.strip() for line in file]
        
        random.shuffle(easy_words)
        
        selected_words = easy_words[:300]
        return selected_words
    else:
        w = RandomWord()
        return [w.word(word_max_length=7) for _ in range(300)]
    
def hard_words():
    hard_words_path = 'hardWords.txt'

    if os.path.exists(hard_words_path):
        with open(hard_words_path, 'r') as file:
            hard_words = [line.strip() for line in file]
        
        random.shuffle(hard_words)
        
        selected_words = hard_words[:300]
        return selected_words
    else:
        w = RandomWord()
        return [w.word(word_max_length=9) for _ in range(300)]