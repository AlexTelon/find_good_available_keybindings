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
    print()

    # left - right side combo. So if first is on left, then second must be on right
    is_left = lambda c: c in left_side_letters
    #is_right = lambda c: c in right_side_letters
    both_sides = lambda pair: is_left(pair[0]) != is_left(pair[1])

    most_common = [(pair,count) for pair, count in most_common if both_sides(pair)]
    print(len(most_common))
    print(most_common[:2])
    print(most_common[-2:])

    # TODO add special chars as unused pairs in most_common? sure . and ; are used somewhat but still they should be added

    # We still have plenty of options here. Lets narrow down to only use letters on the
    # easiest to reach rows. Those where SDF and JKL reside.
    # again removed special chars.
    easy_to_reach = 'wersdfxcv' + 'uiojklm'
    is_easy = lambda c: c in easy_to_reach
    # Note that the first letter is on the homerow already so wont check that.
    most_common = [(pair,count) for pair, count in most_common if is_easy(pair[1])]
    print(len(most_common))
    print(most_common[:2])
    print(most_common[-2:])
    print()

    def as_shortcut(pair):
        translate_table = {
            's': 'Shift',
            'l': 'Shift',
            'd': 'Alt',
            'k': 'Alt',
            'f': 'Ctrl',
            'j': 'Ctrl',
        }
        return f"{translate_table[pair[0]]} + {pair[1].upper()}"

    for pair, count in most_common[-10:]:
        print(as_shortcut(pair))

    # both_in_homerow = lambda pair: pair[0] in home_row and pair[1] in home_row
    # End goal.
    # home_row_side + letter on other side that is easy to reach
    # Then manually choose what feels good and is not already taken.