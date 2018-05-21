

def break_words(stuff):
    words=stuff.split(' ')
    return(words)

def sorted_word(words):
    return sorted(words)

def print_first_word(words):
    word=words.pop(0)
    print(word)

def print_last_word(words):
    word=words.pop(-1)
    print(word)

def sort_senternce(sentence):
    words=break_words(sentence)
    return(sorted_word(words))

def print_first_and_last(sentence):
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words=sort_senternce(sentence)
    print_first_word(words)
    print_last_word(words)
