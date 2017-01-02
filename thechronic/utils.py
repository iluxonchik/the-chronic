from collections import Iterable

def is_iterable(arg):
    """
    Checks if the provided argument is an iterable and not a string.
    """
    return not isinstance(arg, str) and isinstance(arg, Iterable)
