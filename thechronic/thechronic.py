from itertools import chain, product
from thechronic.utils import is_iterable

class TheChronic(object):
    def __init__(self, words=[], files=[]):
        self._parse_words_arg(words)
        self._parse_files_arg(files)

    def combine(self, num_words=1, build_up=False):

        if build_up:
            iterators = ()
            for i in range(1, num_words + 1):
                res = product(self._words, repeat=i)
                iterators += (self._get_words_generator(res),)
            return chain(*iterators)

        res = product(self._words, repeat=num_words)

        return self._get_words_generator(res)

    def _get_words_generator(self, words):
        for word_parts in words:
            yield ''.join(word_parts)

    def _parse_words_arg(self, words):
        if is_iterable(words):
            if len(words) > 0 and is_iterable(words[0]):
                # we have an iterable of iterables (ex: a list of lists)
                self._words = list(chain.from_iterable(words))
            else:
                self._words = list(words)
        else:
            raise ValueError('Invalid argument for \'words\'.')

    def _parse_files_arg(self, files):
        if not is_iterable(files):
            files = (files,)

        for f in files:
            with open(f, mode='r') as wfile:
                file_words = wfile.read().splitlines()
                self._words += file_words
