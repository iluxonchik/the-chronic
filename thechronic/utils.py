from collections import Iterable

def is_iterable(arg):
    """
    Checks if the provided argument is an iterable and not a string.
    """
    return not isinstance(arg, str) and isinstance(arg, Iterable)

def combine_generators(gen1, gen2):
    """
    Combines two generators. For every element in gen1 it adds every element
    from gen2.
    """
    gen2 = list(gen2)

    if len(gen1) == 0:
        gen2 = ['']

    for elem1 in gen1:
        for elem2 in gen2:
            yield elem1 + elem2
