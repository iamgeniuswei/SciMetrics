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

class CoMatrix(object):
    '''
    @description: 构建共现矩阵
    @param {List} 以['A;B;',...]形式形成的数据列表 
    @return: 
    {dict}以字典形式存储的'A;B;...;'第一个数据（A）出现次数
    {dict}以字典形式存储的'A;B;...;'除第一个数据（A）外其他数据出现次数
    {dict}以字典形式存储稀疏共现矩阵，key：'共现A,共现B',value:共现次数
    '''
    def build_matrix(self, data_list):
        first_items = {}
        other_items = {}
        item_groups = {}
        for item in data_list:
            try:
                str_data_list = item.rstrip(';').split(';')
                # 区分第一作者和共同作者，将第一作者和共同作者的频次独立处理
                first_item = str_data_list[0]
                if first_item in first_items:
                    first_items[first_item] += 1
                else:
                    first_items[first_item] = 1
                # 统计共同作者的文章频次，并且构建与第一作者的共现矩阵
                # 一般来说，只统计第一作者与共同作者之间的共现，不统计共同作者之间的共现
                for other_item in str_data_list[1:]:
                    if other_item in other_items:
                        other_items[other_item] += 1
                    else:
                        other_items[other_item] = 1
                    A, B = first_item, other_item
                    # 固定共现序列，以比较序小的在前
                    if A > B :
                        A, B = B, A
                    key = A+","+B
                    if key in item_groups:
                        item_groups[key] += 1
                    else:
                        item_groups[key] = 1
            except Exception as e:
                pass
        return first_items, other_items, item_groups



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
            
# from core.cnki_parser import *
# import networkx as nx
# import matplotlib
# import matplotlib.pyplot as plt
# # %matplotlib inline
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['font.family']='sans-serif'
# import numpy as np
#
# path = "F:\\002-测试数据\\NewNetworkAttack\\input\\CNKI-637293898682050000.xlsx"
# analyzer = SciMetricsAnalyzer('CNKI', path, None)
# analyzer.analyze_source_data()
#
# authors = []
# for article in analyzer.articles:
#     author = article.elements[3]
#     authors.append(author)
#
# g = nx.Graph()
# matrix = CoMatrix()
# first, co, groups = matrix.build_matrix(authors)
# # g.add_node('王豫')
# for key in groups.keys():
#     author_list = key.split(',')
#     g.add_edge(author_list[0], author_list[1])
#
# degrees = g.degree()
# degrees = sorted(degrees, key=lambda x:(x[1]), reverse=True)
# for item in degrees:
#     print('{} - {}'.format(item[0],item[1]))
# # pos = nx.spring_layout(g, k=3, iterations=20)
# # plt.figure(3, figsize=(30, 30))
# nx.draw(g, with_labels=True)
# # nx.draw(g, with_labels=True)
# plt.show()

