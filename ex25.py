def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(A_to_Z):
    """Sorts the words."""
    return sorted(A_to_Z)

def print_first_word(first_word):
    """Prints the first word after popping it off."""
    word = first_word.pop(0)
    print(word)

def print_last_word(last_word):
    """Prints the last word after popping it off."""
    word = last_word.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
