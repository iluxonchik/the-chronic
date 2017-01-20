"""
Module containig combinator implementations and interface.
"""
from itertools import product
from abc import ABCMeta, abstractmethod

from thechronic.utils import is_iterable, combine_generators

class Combinator(metaclass=ABCMeta):
    @abstractmethod
    def get_generator(self, words):
        pass

class NumericCombinator(Combinator):
    def __init__(self, num_digits, build_up):
        self._DIGTIS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        self._num_digits = num_digits
        self._build_up = build_up

    def get_generator(self, words):
        generators = ()
        if self._build_up:
            words = list(words)
            for i in range(1, self._num_digits + 1):
                num_generator = product(self._DIGTIS, repeat=i)
                res = combine_generators(words, num_generator)
                generators += (res,)
        else:
            num_generator = product(self._DIGTIS, repeat=self._num_digits)
            generators += (combine_generators(words, num_generator),)
        return generators
