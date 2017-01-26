"""
Module containig combinator implementations and interface.
"""
from itertools import product, tee
from abc import ABCMeta, abstractmethod

from thechronic.utils import is_iterable

class Combinator(metaclass=ABCMeta):
    @abstractmethod
    def get_iterators(self, words):
        pass

class NumericCombinator(Combinator):
    def __init__(self, num_digits, build_up):
        self._DIGTIS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        self._num_digits = num_digits
        self._build_up = build_up

    def get_iterators(self, words):
        iterators = ()
        begin_range = 1

        if not self._build_up:
            begin_range = self._num_digits
            words = (words,)
        else:
            words = tee(words, self._num_digits + 1 - begin_range)

        index = 0
        for i in range(begin_range, self._num_digits + 1):
            num_generator = product(self._DIGTIS, repeat=i)
            res = product(words[index], num_generator)
            iterators += (res,)
            index += 1

        return iterators
