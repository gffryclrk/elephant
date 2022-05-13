""" The classic elephant
Solve for combinations of letters
This time, by binary counting """

import pdb

def combine_lists(letters, inclusions):
    """ This fn takes two lists and returns a string
    of letters from the first list if their respective
    elements are included in the second list """

    o = []
    for idx, x in enumerate(letters):
        if inclusions[idx]: o.append(x)

    return ''.join(o)

def combinations(word):
    """ Given a word, generate combinations of letters """
    letters = list(word)
    combinations = int(('1' * len(letters)), 2) # Binary representation of all letters, ie 111 for 'cat'

    for a in range(1, combinations+1): # range fn returns [a, b) whereas I want (a, b]
#       pdb.set_trace()
        bit_map = bin(a)[2:].zfill(len(letters))
        yield combine_lists(letters, [int(i) for i in list(bit_map)])
