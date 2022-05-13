""" The classic elephant
Solve for combinations of letters
This time, by binary counting """

def combine_lists(letters, inclusions):
    """ This fn takes two lists and returns a string
    of letters from the first list if their respective
    elements are included in the second list """

    o = []
    for idx, x in enumerate(letters):
        if inclusions[idx]: o.append(x)

    return ''.join(o)

