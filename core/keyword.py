from .base import *
class Keyword(object):
    def __init__(self, name, year):
        self._name = name
        self._freq = 1
        self._year = year

    def get_freq(self):
        return self._freq

    def get_name(self):
        return self._name

    def add_freq(self, increment):
        self._freq += increment

    def update_year(self, year):
        if self._year > year:
            self._year = year



class KeywordCoOccurance(CoOccurance):
    def __init__(self, keyword_a, keyword_b):
        CoOccurance.__init__(self, keyword_a, keyword_b)