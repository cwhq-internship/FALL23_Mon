import wonderwords
from wonderwords import RandomSentence, RandomWord

def create_sentence(length):
    text = []
    for i in range(0,length):
        s = RandomSentence()
        text.append(s.sentence())
    
    return text

def easy_words():
    w = RandomWord()
    text = [w.word(word_max_length=4) for _ in range(30)]
    return text

def medium_words():
    text = []
    for i in range(0,25):
        s = RandomSentence()
        w = RandomWord()
        text.append(w.word(word_min_length=7, word_max_length=11))

    return text

def hard_words():
    text = []
    for i in range(0,20):
        s = RandomSentence()
        w = RandomWord()
        text.append(w.word(word_min_length=14))
    return text


