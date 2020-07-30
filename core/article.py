'''
@Author: your name
@Date: 2020-07-27 11:15:07
@LastEditTime: 2020-07-27 11:15:07
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \SciMetrics\core\article.py
'''

from .utils import *


class Article(object):
    def __init__(self, csv_data:list):
        try:
            self._authors = format_str(csv_data[2])
            self._institutes = format_str(csv_data[3])
            self._title = csv_data[4]
            self._journal = csv_data[5]
            self._year = csv_data[6]
            self._keywords = format_str(csv_data[10])
            self._abstract = csv_data[11]
        except Exception as e:
            print(str(e))

    def get_authors(self):
        return self._authors

    def get_institutes(self):
        return self._institutes

    def get_title(self):
        return self._title

    def get_year(self):
        return self._year

    def get_keywords(self):
        return self._keywords

    def get_abstract(self):
        return self._abstract