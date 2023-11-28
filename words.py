from wonderwords import RandomSentence, RandomWord

def create_sentence(length):
    text = []
    for i in range(0,length):
        s = RandomSentence()
        text.append(s.sentence())
    
    return text

def easy_words():
    text = []
    for i in range(0,100):
        s = RandomSentence()
        w = RandomWord()
        text.append(w.word(word_max_length=4))
    
    return text

def medium_words():
    text = []
    for i in range(0,100):
        s = RandomSentence()
        w = RandomWord()
        text.append(w.word(word_min_length=7, word_max_length=11))

    return text

def hard_words():
    text = []
    for i in range(0,100):
        s = RandomSentence()
        w = RandomWord()
        text.append(w.word(word_min_length=14))
    return text


