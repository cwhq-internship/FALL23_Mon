from wonderwords import RandomSentence

def create_sentence(length):
    text = []
    for i in range(0,length):
        s = RandomSentence()
        text.append(s.sentence())
    
    return text


