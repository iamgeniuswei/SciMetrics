import sys
import os
import openpyxl
import pandas as pd
class CNKIFormatItem(object):
    def __init__(self):
        self.elements = []

from dataclasses import dataclass
from typing import List

@dataclass
class Article(object):
    elements:List[str]
    # RT:str
    # SR:str
    # A1:str
    # AD:str
    # T1:str
    # TF:str
    # YR:str
    # IS:str
    # vo:str
    # OP:str
    # K1:str
    # AB:str
    # SN:str
    # CN:str
    # LA:str
    # DS:str

@dataclass
class Author(object):
    name:str
    articles:List[Article]
    article_count:int


def format_parser_helper(path, format):
    try:
        files = os.listdir(path)
        for file in files:
            if format == 'CNKI':
                parser = CNKIFormatParser()
                parser.parse_cnki_files(file)
    except Exception as e:
        print(str(e))


class SciMetricsAnalyzer(object):
    def __init__(self, format, data_path, project_path):
        self.format = format
        self.data_path = data_path
        self.project_path = project_path
        self.articles = []
        self.analyze_source_data()
        self.authors = {}

    def analyze_source_data(self):
        try:
            # files = os.listdir(self.data_path)
            # for file in files:
            if self.format == 'CNKI':
                parser = CNKIFormatParser()
                self.articles = parser.parse_cnki_files(self.data_path)
        except Exception as e:
            print(str(e))


    def analyze_authors(self):
        for article in self.articles:
            try:
                str_authors = article.elements[2]
                str_authors_list = str_authors.rstrip(';').split(';')
                for str_author in str_authors_list:
                    if str_author in self.authors:
                        self.authors[str_author].articles.append(article)
                        self.authors[str_author].article_count += 1
                    else:
                        author = Author(str_author, [], 0)
                        author.articles.append(article)
                        author.article_count = 1
                        self.authors[str_author] = author
            except Exception as e:
                print(str(e))
        # sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
        # lambda x: expression
        self.authors = sorted(self.authors.items(), key=lambda x: x[1].article_count, reverse=True)
        print(self.authors)
        print('OK')
        



class CNKIFormatParser(object):
    def __init__(self):
        pass

    def parse_cnki_files(self, file):
        try:
            wb = openpyxl.load_workbook(file)
            ws = wb.active
            rows = ws.max_row   
            columns = ws.max_column         
            cnki_items = []
            chinese = True
            for row in range(2, rows+1):
                guard = ws.cell(row, 1).value
                if guard == None:
                    continue
                elif guard == 'RT':
                    chinese = False
                    continue
                if chinese is True:
                    item = Article([])
                    for column in range(1, columns):                    
                        item.elements.append(ws.cell(row=row, column=column).value)
                elif chinese is False:
                    item = Article([])
                    for column in range(1, 10):                    
                        item.elements.append(ws.cell(row=row, column=column).value)
                    item.elements.append(None)
                    item.elements.append(ws.cell(row=row, column=10).value)
                    item.elements.append(ws.cell(row=row, column=11).value)  
                    item.elements.append(None)
                    item.elements.append(None)
                    item.elements.append(None)
                    item.elements.append(ws.cell(row=row, column=12).value)
                cnki_items.append(item)
            return cnki_items
        except Exception as e:
            print(str(e))


# if __name__ == '__main__':
path = "F:\\002-测试数据\\NewNetworkAttack\\input\\CNKI-637293898682050000.xlsx"
analyzer = SciMetricsAnalyzer('CNKI', path, None)
analyzer.analyze_authors()

# authors = {}

# authors['A'] = 1
# authors['B'] = 2
# authors['C'] = 7
# authors['D'] = 4
# authors = sorted(authors.items(), key=lambda x: x[1], reverse=True)

# print(authors)