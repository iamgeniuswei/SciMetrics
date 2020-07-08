import wx

from GUI.listview import *
from GUI.main_windows import *
from GUI.comatrix_view import *
from core.cnki_parser import *
from core.co_occurance_matrix import *
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':
   # 下面是使用wxPython的固定用法


   # %matplotlib inline
   matplotlib.rcParams['font.sans-serif'] = ['SimHei']
   matplotlib.rcParams['font.family'] = 'sans-serif'


   # authors = ['王豫;高凤娟;马可欣;司徒凌云;王林章;陈碧欢;刘杨;赵建华;李宣东;','孙子文;张书国;王林章;', '张蔚瑶;张磊;毛建瓴;许智君;张玉军;','李永成;刘树美;于尧;李爽;李宣东;']

   path = "F:\\002-测试数据\\NewNetworkAttack\\input\\CNKI-637293898682050000.xlsx"
   analyzer = SciMetricsAnalyzer('CNKI', path, None)
   analyzer.analyze_source_data()

   authors = []
   for article in analyzer.articles:
       author = article.elements[3]
       authors.append(author)

   g = nx.Graph()
   matrix = CoMatrix()
   first, co, groups = matrix.build_matrix(authors)
   # g.add_node('王豫')
   for key in groups.keys():
       author_list = key.split(',')
       g.add_edge(author_list[0], author_list[1])

   degrees = g.degree()
   degrees = sorted(degrees, key=lambda x: (x[1]), reverse=True)

   app = wx.App()
   main_win = CoMatrixView(None)
   main_win.renderMatrix(degrees)
   main_win.Show()
   app.MainLoop()