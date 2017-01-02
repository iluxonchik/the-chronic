"""
Conatins utils used in test files.
"""

def gen_len(gen):
    """
    Get genreator's length.
    """
    return sum(1 for _ in gen)

def get_words_generator(words):
    for word_parts in words:
        yield ''.join(word_parts)
