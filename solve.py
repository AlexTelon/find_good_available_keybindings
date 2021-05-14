from collections import Counter
import random

def load_words():
    # Example from the submodule
    with open('english-words/words_alpha.txt') as f:
        return set(f.read().split())

def char_pairs(word):
    """Returns all the char pairs in order of the word.
    
    It includes pair for the last char with ''.

    Examples:
    'a' -> ('a', '')
    'ab' -> ('a', 'b')
            ('b', '')
    """
    return zip(word, list(word[1:]) + [''])

if __name__ == '__main__':
    words = load_words()

    # for testing, lets sample to speed things up.
    words = random.sample(words, 2000)

    c_pairs = [c for word in words for c in char_pairs(word)]
    count = Counter(c_pairs)

    print(count.most_common(5))
    print(count.most_common()[-5:])
