class Strange(object):
    """
    Wrapper arround the built-in range() function, which returns str instead of
    int on iteration.

    Just like a range object, an instance of Srange can be iterated over
    multiple times.
    """

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0
        self._range = range(start, stop, step)
        self._iter = iter(self._range)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            str_num = str(next(self._iter))
        except StopIteration as err:
            self._iter = iter(self._range)
            raise err
        return str_num
