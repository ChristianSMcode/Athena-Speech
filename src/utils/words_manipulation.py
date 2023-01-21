from fuzzywuzzy import fuzz

def compare_words_simil(word_a,word_b):
    return fuzz.ratio(word_a, word_b)