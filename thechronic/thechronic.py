from itertools import chain, product

from thechronic.utils import is_iterable
from thechronic.combinators import NumericCombinator

class TheChronic(object):
    def __init__(self, words=[], files=[], separator=''):
        self._parse_words_arg(words)
        self._parse_files_arg(files)
        self._separator = separator
        self._numeric = None

    def combine(self, num_words=1, build_up=False, min_length=1, max_length=None):
        if len(self._words) == 0:
            self._words = ['']
        self._min_length = min_length
        self._max_length = max_length
        iterators = ()
        begin_range = 1 if build_up else num_words

        for i in range(begin_range, num_words + 1):
            res = product(self._words, repeat=i)
            iterators += (self._get_words_generator(res, min_length, max_length),)
            # re-create generator, since the prevoius one is used up top
            res = product(self._words, repeat=i)
            iterators += self._get_numeric_generators(res, min_length, max_length)

        return chain(*iterators)

    def add_numeric(self, digits=1, build_up=False):
        self._numeric = NumericCombinator(digits, build_up)

    def _get_numeric_combinations_generator(self, words):
        if self._numeric:
            return self._numeric.get_iterators(words)
        else:
            return ()

    def _get_words_generator(self, words, min_length, max_length):
        for word_parts in words:
            word = self._tuple_to_word(word_parts)
            if self._is_word_within_limits(word, min_length, max_length):
                yield word

    def _tuple_to_word(self, t):
        # NOTE: some empirical tests showed that having this funciton
        # negatively affects the performance a little bit (I assume this is due
        # to the call stack). If some 'crazy'optimizaitons are needed in the
        # future, consider removing it and joining the tuple inline.
        # Almost certainly, removing it won't be necessary, but I'm leaving this
        # note here since this function is called quite a lot.
        return self._separator.join(t)

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

    def _get_words_generator_from_num_iterator(self, iterator):
        """
        Each `iterator` is a pair of two tuples.
        """
        for tuple_pair in iterator:

            tuple_sum = ()
            for t in tuple_pair:
                tuple_sum += t

            word = self._tuple_to_word(tuple_sum)
            yield word

    def _get_numeric_generators(self, words, min_length, max_length):
        generators = ()
        if self._numeric:
            num_comb = self._get_numeric_combinations_generator(words)
            for iterator in num_comb:
                gen = self._get_words_generator_from_num_iterator(iterator)
                generators += (gen,)
        return generators
