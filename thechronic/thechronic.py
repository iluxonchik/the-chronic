from itertools import chain, product
from thechronic.utils import is_iterable

class TheChronic(object):
    def __init__(self, words):
        if is_iterable(words):
            if is_iterable(words[1]):
                # we have an iterable of iterables (ex: a list of lists)
                self._words = list(chain.from_iterable(words))
            else:
                self._words = list(words)
        else:
            raise ValueError('Invalid argument for \'words\'.')

    def combine(self, num_words=1):
        res = product(self._words, repeat=num_words)

        return self._get_words_generator(res)

    def _get_words_generator(self, words):
        for word_parts in words:
            yield ''.join(word_parts)
