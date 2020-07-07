'''
......................................&&.........................
....................................&&&..........................
.................................&&&&............................
...............................&&&&..............................
.............................&&&&&&..............................
...........................&&&&&&....&&&..&&&&&&&&&&&&&&&........
..................&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&..............
................&...&&&&&&&&&&&&&&&&&&&&&&&&&&&&.................
.......................&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&.........
...................&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&...............
..................&&&   &&&&&&&&&&&&&&&&&&&&&&&&&&&&&............
...............&&&&&@  &&&&&&&&&&..&&&&&&&&&&&&&&&&&&&...........
..............&&&&&&&&&&&&&&&.&&....&&&&&&&&&&&&&..&&&&&.........
..........&&&&&&&&&&&&&&&&&&...&.....&&&&&&&&&&&&&...&&&&........
........&&&&&&&&&&&&&&&&&&&.........&&&&&&&&&&&&&&&....&&&.......
.......&&&&&&&&.....................&&&&&&&&&&&&&&&&.....&&......
........&&&&&.....................&&&&&&&&&&&&&&&&&&.............
..........&...................&&&&&&&&&&&&&&&&&&&&&&&............
................&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&............
..................&&&&&&&&&&&&&&&&&&&&&&&&&&&&..&&&&&............
..............&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&....&&&&&............
...........&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&......&&&&............
.........&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&.........&&&&............
.......&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&...........&&&&............
......&&&&&&&&&&&&&&&&&&&...&&&&&&...............&&&.............
.....&&&&&&&&&&&&&&&&............................&&..............
....&&&&&&&&&&&&&&&.................&&...........................
...&&&&&&&&&&&&&&&.....................&&&&......................
...&&&&&&&&&&.&&&........................&&&&&...................
..&&&&&&&&&&&..&&..........................&&&&&&&...............
..&&&&&&&&&&&&...&............&&&.....&&&&...&&&&&&&.............
..&&&&&&&&&&&&&.................&&&.....&&&&&&&&&&&&&&...........
..&&&&&&&&&&&&&&&&..............&&&&&&&&&&&&&&&&&&&&&&&&.........
..&&.&&&&&&&&&&&&&&&&&.........&&&&&&&&&&&&&&&&&&&&&&&&&&&.......
...&&..&&&&&&&&&&&&.........&&&&&&&&&&&&&&&&...&&&&&&&&&&&&......
....&..&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&...........&&&&&&&&.....
.......&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&..............&&&&&&&....
.......&&&&&.&&&&&&&&&&&&&&&&&&..&&&&&&&&...&..........&&&&&&....
........&&&.....&&&&&&&&&&&&&.....&&&&&&&&&&...........&..&&&&...
.......&&&........&&&.&&&&&&&&&.....&&&&&.................&&&&...
.......&&&...............&&&&&&&.......&&&&&&&&............&&&...
........&&...................&&&&&&.........................&&&..
.........&.....................&&&&........................&&....
...............................&&&.......................&&......
................................&&......................&&.......
.................................&&..............................
..................................&..............................
'''



'''
@Author: your name
@Date: 2020-07-07 09:24:39
@LastEditTime: 2020-07-07 09:30:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \SciMetrics\core\co_occurance_matrix.py
'''
# coding=utf-8

class Matrix(object):
    '''共现矩阵'''
    def test(self):
        pass


class CoAuthorMatrix(object):

    def __init__(self):
        pass

    '''
    @description: 构建作者共现矩阵
    @param {List}以['作者A;作者B;',...]形式形成的作者列表 
    @return: 
    '''
    def build_matrix(self, authors_list):
        first_authors = {}
        co_authors = {}
        author_groups = {}
        for item in authors_list:
            try:
                str_authors_list = item.rstrip(';').split(';')
                # 区分第一作者和共同作者，将第一作者和共同作者的频次独立处理
                first_author = str_authors_list[0]
                if first_author in first_authors:
                    first_authors[first_author] += 1
                else:
                    first_authors[first_author] = 1
                # 统计共同作者的文章频次，并且构建与第一作者的共现矩阵
                # 一般来说，只统计第一作者与共同作者之间的共现，不统计共同作者之间的共现
                for author in str_authors_list[1:]:
                    if author in co_authors:
                        co_authors[author] += 1
                    else:
                        co_authors[author] = 1
                    A, B = first_author, author
                    # 固定共现序列，以比较序小的在前
                    if A > B :
                        A, B = B, A
                    key = A+","+B
                    if key in author_groups:
                        author_groups[key] += 1
                    else:
                        author_groups[key] = 1
            except Exception as e:
                pass
        return first_authors, co_authors, author_groups
            
from core.cnki_parser import *
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline
matplotlib.rcParams['font.sans-serif'] = ['SimHei']   
matplotlib.rcParams['font.family']='sans-serif'
import numpy as np
# authors = ['王豫;高凤娟;马可欣;司徒凌云;王林章;陈碧欢;刘杨;赵建华;李宣东;','孙子文;张书国;王林章;', '张蔚瑶;张磊;毛建瓴;许智君;张玉军;','李永成;刘树美;于尧;李爽;李宣东;']

path = "F:\\002-测试数据\\NewNetworkAttack\\input\\CNKI-637293898682050000.xlsx"
analyzer = SciMetricsAnalyzer('CNKI', path, None)
analyzer.analyze_source_data()

authors = []
for article in analyzer.articles:
    author = article.elements[2]
    authors.append(author)

g = nx.Graph()
matrix = CoAuthorMatrix()
first, co, groups = matrix.build_matrix(authors)
# g.add_node('王豫')
for key in groups.keys():
    author_list = key.split(',')
    g.add_edge(author_list[0], author_list[1])


# pos = nx.spring_layout(g, k=3, iterations=20)
# plt.figure(3, figsize=(30, 30))
nx.draw(g, with_labels=True)
# nx.draw(g, with_labels=True)
plt.show()
