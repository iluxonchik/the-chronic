"""
Conatins utils used in test files.
"""

def gen_len(gen):
    """
    Get genreator's length.
    """
    return sum(1 for _ in gen)
