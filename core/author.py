'''
@Author: your name
@Date: 2020-07-27 11:05:18
@LastEditTime: 2020-07-27 11:06:07
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \SciMetrics\core\author.py
'''

class AuthorOccurance(object):
    """作者共现类"""
    def __init__(self, author_a, author_b):
        self._author_a = author_a
        self._author_b = author_b
        self._occurance = 1

    def add_occurance(self, increment):
        self._occurance += increment

    def get_occurance(self):
        return self._occurance

    def get_authors(self):
        return self._author_a + ';' + self._author_b

class Author(object):
    """作者类"""
    def __init__(self, name, institute=None):
        self._name = name
        self._institute = institute
        self._freq_all = 0
        self._freq_first = 0
        self._freq_other = 0

    def get_institute(self):
        return self._institute

    def get_name(self):
        return self._name

    def _set_freq_all(self, freq_all):
        self._freq_all = freq_all

    def _add_freq_all(self, increment):
        self._freq_all += increment

    def get_freq_all(self):
        return self._freq_all

    def set_freq_first(self, freq_first):
        self._freq_all -= self._freq_first
        self._freq_first = freq_first
        self._freq_all += self._freq_first


    def add_freq_first(self, increment):
        self._freq_first += increment
        self._freq_all += increment

    def get_freq_first(self):
        return self._freq_first

    def set_freq_other(self, freq_other):
        self._freq_all -= self._freq_other
        self._freq_other = freq_other
        self._freq_all += self._freq_other

    def add_freq_other(self, increment):
        self._freq_other += increment
        self._freq_all += increment

    def get_freq_other(self):
        return self._freq_other