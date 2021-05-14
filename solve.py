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
    counter = Counter(c_pairs)

    # not a true homerow, but these are the dual function keys I have and care about right now.
    home_row = 'sdfjkl'
    home_row_left, home_row_right = 'sdf', 'jkl'

    left_side_letters =  'qwertasdfgzxcvb'
    right_side_letters = 'yuiophjklnm' # removed special chars, they are not present in words anyways


    most_common = counter.most_common()
    print(len(most_common))
    print()

    # Remove last letter pairs.
    most_common = [(pair,count) for pair, count in most_common if pair[1] != '']
    print(len(most_common))
    print(most_common[:2])
    print(most_common[-2:])
    print()

    # Only care if first is in home row.
    most_common = [(pair,count) for pair, count in most_common if pair[0] in home_row]
    print(len(most_common))
    print(most_common[:2])
    print(most_common[-2:])


    # both_in_homerow = lambda pair: pair[0] in home_row and pair[1] in home_row
    # End goal.
    # home_row_side + letter on other side that is easy to reach
    # Then manually choose what feels good and is not already taken.