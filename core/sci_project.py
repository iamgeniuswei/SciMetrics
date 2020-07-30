'''
@Author: your name
@Date: 2020-07-27 14:37:33
@LastEditTime: 2020-07-27 14:37:33
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \SciMetrics\core\sci_project.py
'''

import os
import os.path
import pandas as pd
import math
from .article import *
from .author import *
from .institute import *
from .keyword import *

class SciProjectController(object):
    def __init__(self, config_file=None):
        pass

    def get_configuration_from_file(self, config_file):
        pass

    def set_input_directory(self, input_dir):
        self._input_dir = input_dir

    def get_input_dir(self):
        return self._input_dir

    def set_project_directory(self, project_dir):
        self._project_dir = project_dir

    def get_project_dir(self):
        return self._project_dir

    def get_author_occurance_type(self):
        return 'B'





class SciProject(object):
    def __init__(self):
        self._controller = SciProjectController()
        self.articles = dict()
        self._authors = dict()
        self._authors_occurance = dict()
        self._institutes = dict()
        self._keywords = dict()
        self._keywords_cooccurance = dict()

    def set_configuration(self):
        self._controller.set_input_directory("F:\\tesproject\\output")



    def get_articles_from_csv(self):
        try:
            for file in os.listdir(self._controller.get_input_dir()):
                file_path = os.path.join(self._controller.get_input_dir(), file)
                csv_file = pd.read_excel(file_path)
                max_rows = csv_file.shape[0]
                for index in range(0, max_rows):
                    new_article = Article(csv_file.iloc[index].values)
                    new_article_item = {new_article.get_title(): new_article}
                    self.articles.update(new_article_item)
        except Exception as e:
            print(str(e))


    def print_authors_occurance(self):
        authors_occurance = sorted(self._authors_occurance.values(), key=lambda x: x.get_occurance(), reverse=True)
        for item in authors_occurance:
            print("{} - {}".format(item.get_authors(), item.get_occurance()))

    def print_authors(self):
        for item in self._authors.items():
            print("{} - {}".format(item[0], item[1].get_freq_all()))

    def get_authors_occurance(self, authors_list:list):
        """
        根据['A' 'B' 'C' 'D']形式表示的作者列表计算作者共现
        类函数，计算结果保存在self._authors_occurance = dict()中
        @param authors_list:
        """
        if self._controller.get_author_occurance_type() == 'A':
            first_author = authors_list[0]
            for other_author in authors_list[1:]:
                A, B = first_author, other_author
                # 固定共现序列，以比较序小的在前
                if A > B:
                    A, B = B, A
                key = A + ';' + B
                if key in self._authors_occurance:
                    authors_occurance = self._authors_occurance[key]
                    authors_occurance.add_occurance(1)
                else:
                    authors_occurance = AuthorOccurance(A, B)
                    self._authors_occurance[key] = authors_occurance
        else:
            for i in range(0,len(authors_list)-1):
                for j in range(i+1, len(authors_list)):
                    A, B = authors_list[i], authors_list[j]
                    if A > B:
                        A, B = B, A
                    key = A + ';' + B
                    if key in self._authors_occurance:
                        authors_occurance = self._authors_occurance[key]
                        authors_occurance.add_occurance(1)
                    else:
                        authors_occurance = AuthorOccurance(A, B)
                        self._authors_occurance[key] = authors_occurance


    def get_authors(self):
        try:
            for article in self.articles.values():
                authors_list = article.get_authors().split(';')
                authors_list = list(filter(None, authors_list))
                if article.get_institutes() is not None:
                    institute_list = article.get_institutes().split(';')
                    str_first_author_institute = institute_list[0]
                else:
                    str_first_author_institute = None
                # 处理第一作者
                str_first_author = authors_list[0]
                if str_first_author in self._authors:
                    first_author = self._authors[str_first_author]
                    first_author.add_freq_first(1)
                else:
                    first_author = Author(str_first_author, str_first_author_institute)
                    first_author.add_freq_first(1)
                    self._authors[str_first_author] = first_author

                # 处理其他挂名作者
                for str_other_author in authors_list[1:]:
                    if str_other_author in self._authors:
                        other_author = self._authors[str_other_author]
                        other_author.add_freq_other(1)
                    else:
                        other_author = Author(str_other_author)
                        other_author.add_freq_other(1)
                        self._authors[str_other_author] = other_author

                self.get_authors_occurance(authors_list)
        except Exception as e:
            print(str(e))


    def get_institutes(self):
        try:
            for article in self.articles.values():
                self.calcuate_institute(article.get_institutes())
        except Exception as e:
            print(str(e))



    def print_keywords(self):
        keywords = sorted(self._keywords.values(), key=lambda x: x.get_freq(), reverse=True)
        for keyword in keywords:
            print('{}-{}'.format(keyword.get_name(), keyword.get_freq()))

    def get_keywords(self):
        try:
            for article in self.articles.values():
                self.calculate_keywords(article.get_keywords(), article.get_year())
        except Exception as e:
            print(str(e))


    def print_keywords_cooccurance(self):
        keywords_cooccurance = sorted(self._keywords_cooccurance.values(), key=lambda x:x.get_occurance(), reverse=True)
        for item in keywords_cooccurance:
            print('{}-{}'.format(item.get_keys(), item.get_occurance()))

    def calculate_keywords_occurance(self, keywords_list:list):
        """
        根据['A' 'B' 'C' 'D']形式表示的关键字列表计算关键字共现
        类函数，计算结果保存在self.keywords_cooccurance = dict()中
        @param keywords_list: ['A' 'B' 'C' 'D']形式表示的关键字列表
        """
        for i in range(0, len(keywords_list) - 1):
            for j in range(i + 1, len(keywords_list)):
                A, B = keywords_list[i], keywords_list[j]
                if A > B:
                    A, B = B, A
                key = A + ';' + B
                if key in self._keywords_cooccurance:
                    keywords_cooccurance = self._keywords_cooccurance[key]
                    keywords_cooccurance.add_occurance(1)
                else:
                    keywords_cooccurance = KeywordCoOccurance(A, B)
                    self._keywords_cooccurance[key] = keywords_cooccurance

    def calculate_keywords(self, keywords_str:str, year:str):
        try:
            keyword_list = keywords_str.split(';')
            keyword_list = list(filter(None, keyword_list))
            for str_keyword in keyword_list:
                if str_keyword in self._keywords:
                    keyword = self._keywords[str_keyword]
                    keyword.add_freq(1)
                    keyword.update_year(year)
                else:
                    keyword = Keyword(str_keyword, year)
                    self._keywords[str_keyword] = keyword
            self.calculate_keywords_occurance(keyword_list)
        except Exception as e:
            print(str(e))

    def calcuate_institute(self, institute_str:str):
        try:
            institute_list = institute_str.split(';')
            institute_list = list(filter(None, institute_list))
            for str_institute in institute_list:
                if str_institute in self._institutes:
                    institute = self._institutes[str_institute]
                    institute.add_freq_articles(1)
                else:
                    institute = Institute(str_institute)
                    self._institutes[str_institute] = institute
        except Exception as e:
            print(str(e))


    def calculate_institute_occurance(self, institute_str:str):
        """
        计算机构共现
        @param institute_str: 以'A;B;C'形式表示的机构列表
        """
        pass

    def print_institutes(self):
        institutes = sorted(self._institutes.values(), key=lambda x:x.get_freq_articles(), reverse=True)
        for item in institutes:
            print("{} - {}".format(item.get_name(), item.get_freq_articles()))


    def calculate_core_authors(self)->list:
        """
        计算核心作者
        @rtype: object
        """
        try:
            authors = sorted(self._authors.values(), key=lambda x: x.get_freq_first(), reverse=True)
            for item in authors:
                print('{}-{}-{}'.format(item.get_name(), item.get_institute() ,item.get_freq_first()))
            return authors
        except Exception as e:
            print(str(e))


    def calculate_core_authors_all(self)->list:
        """
        计算核心作者
        @rtype: object
        """
        try:
            authors = sorted(self._authors.values(), key=lambda x: x.get_freq_all(), reverse=True)
            if len(authors) > 0:
                max_article_count = authors[0].get_freq_all()
                min_article_count = math.ceil(0.749 * math.sqrt(max_article_count))
                print('{}-{}'.format('min_article_count', min_article_count))
                index = 0
                for author in authors:
                    if author.get_freq_all() >= min_article_count:
                        index += 1
                    else:
                        break
                authors = authors[:index]
                for item in authors:
                    print('{}-{}-{}'.format(item.get_name(), item.get_institute(), item.get_freq_all()))
            return authors
        except Exception as e:
            print(str(e))


    # def find_index_in_authors_all(self, items:list, min_article_count)->int:
    #     size = len(items)
    #     found = False
    #     start = 0
    #     end = size - 1
    #     while start < end:
    #         mid = math.floor((start+end)/2)
    #         author = items[mid]
    #         if author.get_freq_all()
