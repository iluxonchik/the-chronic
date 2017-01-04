from itertools import chain, product
from thechronic.utils import is_iterable

class TheChronic(object):
    def __init__(self, words=[], files=[]):
        self._parse_words_arg(words)
        self._parse_files_arg(files)

    def combine(self, num_words=1, build_up=False, min_length=0, max_length=None):
        self._min_length = min_length
        self._max_length = max_length
        if build_up:
            iterators = ()
            for i in range(1, num_words + 1):
                res = product(self._words, repeat=i)
                iterators += (self._get_words_generator(res, min_length, max_length),)
            return chain(*iterators)

        res = product(self._words, repeat=num_words)
        return self._get_words_generator(res, min_length, max_length)

    def _get_words_generator(self, words, min_length, max_length):
        for word_parts in words:
            word = ''.join(word_parts)
            if self._is_word_within_limits(word, min_length, max_length):
                yield word

    def _is_word_within_limits(self, word, min_length, max_length):
        if len(word) >= min_length:
            if max_length is None:
                return True
            elif len(word) <= max_length:
                return True
        return False

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
