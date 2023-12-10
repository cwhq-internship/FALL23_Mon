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

def wordswords():
    word_array = [
    "apple", "banana", "orange", "grape", "kiwi", "strawberry", "blueberry", "watermelon",
    "pineapple", "peach", "pear", "mango", "plum", "cherry", "lemon", "lime", "coconut",
    "pomegranate", "apricot", "nectarine", "raspberry", "blackberry", "cranberry", "fig",
    "guava", "papaya", "melon", "tangerine", "dragonfruit", "lychee", "passionfruit",
    "cantaloupe", "honeydew", "grapefruit", "avocado", "persimmon", "starfruit", "quince",
    "durian", "jackfruit", "kiwifruit", "mulberry", "date", "plantain", "boysenberry",
    "elderberry", "feijoa", "loganberry", "salmonberry", "marionberry", "tamarillo",
    "ugli fruit", "breadfruit", "ackee", "rhubarb", "cherimoya", "soursop", "longan",
    "rambutan", "custard apple", "kumquat", "medlar", "sapodilla", "cherries", "pears",
    "grapes", "plums", "apples", "oranges", "bananas", "kiwis", "lemons", "limes",
    "watermelons", "pineapples", "mangoes", "peaches", "nectarines", "apricots",
    "pomegranates", "strawberries", "blueberries", "blackberries", "raspberries",
    "cranberries", "cherries", "lychees", "passionfruits", "guavas", "papayas", "melons",
    "tangerines", "dragonfruits", "coconuts", "persimmons", "avocados", "grapefruits",
    "figs", "kiwifruits", "pluots", "cherries", "pears", "grapes", "plums", "apples",
    "oranges", "bananas", "kiwis", "lemons", "limes", "watermelons", "pineapples",
    "mangoes", "peaches", "nectarines", "apricots", "pomegranates", "strawberries",
    "blueberries", "blackberries", "raspberries", "cranberries", "cherries", "lychees",
    "passionfruits", "guavas", "papayas", "melons", "tangerines", "dragonfruits",
    "coconuts", "persimmons", "avocados", "grapefruits", "figs", "kiwifruits", "pluots",
    "cherries", "pears", "grapes", "plums", "apples", "oranges", "bananas", "kiwis",
    "lemons", "limes", "watermelons", "pineapples", "mangoes", "peaches", "nectarines",
    "apricots", "pomegranates", "strawberries", "blueberries", "blackberries", "raspberries",
    "cranberries", "cherries", "lychees", "passionfruits", "guavas", "papayas", "melons",
    "tangerines", "dragonfruits", "coconuts", "persimmons", "avocados", "grapefruits",
    "figs", "kiwifruits", "pluots", "cherries", "pears", "grapes", "plums", "apples",
    "oranges", "bananas", "kiwis", "lemons", "limes", "watermelons", "pineapples",
    "mangoes", "peaches", "nectarines", "apricots", "pomegranates", "strawberries",
    "blueberries", "blackberries", "raspberries", "cranberries", "cherries", "lychees",
    "passionfruits", "guavas", "papayas", "melons", "tangerines", "dragonfruits",
    "coconuts", "persimmons", "avocados", "grapefruits", "figs", "kiwifruits", "pluots",
    "cherries", "pears", "grapes", "plums", "apples", "oranges", "bananas", "kiwis",
    "lemons", "limes", "watermelons", "pineapples", "mangoes", "peaches", "nectarines",
    "apricots", "pomegranates", "strawberries", "blueberries", "blackberries", "raspberries",
    "cranberries", "cherries", "lychees", "passionfruits", "guavas", "papayas", "melons",
    "tangerines", "dragonfruits", "coconuts", "persimmons", "avocados", "grapefruits",
    "figs", "kiwifruits", "pluots", "cherries", "pears", "grapes", "plums", "apples",
    "oranges", "bananas", "kiwis", "lemons", "limes", "watermelons", "pineapples",
    "mangoes", "peaches", "nectarines", "apricots", "pomegranates", "strawberries",
    "blueberries", "blackberries", "raspberries", "cranberries", "cherries", "lychees",
    "passionfruits", "guavas", "papayas", "melons", "tangerines", "dragonfruits",
    "coconuts", "persimmons", "avocados", "grapefruits", "figs", "kiwifruits", "pluots"]
    return word_array