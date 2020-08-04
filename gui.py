'''
@Author: your name
@Date: 2020-07-03 09:26:15
@LastEditTime: 2020-07-14 15:24:02
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \SciMetrics\gui.py
'''
# import wx

# from GUI.listview import *
# from GUI.main_windows import *
# from GUI.comatrix_view import *
from GUI.gui_sciview import *
from GUI.gui_listview import *
from core.cnki_parser import *
# from core.co_occurance_matrix import *
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import PySide2
from core.article import *
from core.sci_project import *
from core.data_cleaning import *
from GUI.main_window import *
from pyecharts.charts import Bar
if __name__ == '__main__':
   # 下面是使用wxPython的固定用法


   # project = SciProject()
   # project.set_configuration()
   # project.get_articles_from_csv()
   # project.get_keywords()
   # project.print_keywords_cooccurance()
   # project.get_institutes()
   # project.print_institutes()
   # project.get_authors()
   # project.print_authors()
   # project.print_authors_occurance()
   # project.calculate_core_authors_all()
   # dc = DataCleanning("F:\\tesproject\\translate", "F:\\tesproject\\output")
   # dc.clean_data()
   print('OK')




   # %matplotlib inline
   # matplotlib.rcParams['font.sans-serif'] = ['SimHei']
   # matplotlib.rcParams['font.family'] = 'sans-serif'


   # authors = ['王豫;高凤娟;马可欣;司徒凌云;王林章;陈碧欢;刘杨;赵建华;李宣东;','孙子文;张书国;王林章;', '张蔚瑶;张磊;毛建瓴;许智君;张玉军;','李永成;刘树美;于尧;李爽;李宣东;']

   path = "F:\\002-测试数据\\NewNetworkAttack\\input\\CNKI-637293898682050000.xlsx"
   analyzer = SciMetricsAnalyzer('CNKI', path, None)
   analyzer.analyze_articles()
   authors_stat = analyzer.analyze_authors()
   # headers = ['name', 'freq', 'co']
   # data = []
   # for key, value in authors_stat.items():
   #    item = []
   #    try:
   #       item.append(key)
   #       if 'articleAsFirst' in value:
   #          item.append(value['articleAsFirst'])
   #       else:
   #          item.append(0)
   #       if 'articleAsCo' in value:
   #          item.append(value['articleAsCo'])
   #       else:
   #          item.append(0)
   #       data.append(item)
   #    except Exception as e:
   #       print(str(e))

   print('OK')
   #
   #
   app = QApplication([])
   view = SciView()
   view.setData(authors_stat)
   view.show()
   app.exec_()

   # authors = []
   # for article in analyzer.articles:
   #     author = article.elements[10]
   #     authors.append(author)
   #
   # g = nx.Graph()
   # matrix = CoMatrix()
   # first, co, groups = matrix.build_matrix(authors)
   # for key, value in first.items():
   #    g.add_node(key, size=value)
   # for key in groups.keys():
   #     author_list = key.split(',')
   #     g.add_edge(author_list[0], author_list[1])
   # pos = nx.circular_layout(g)
   # # nodes = g.nodes()
   # #
   # degrees = g.degree()
   # degrees = sorted(degrees, key=lambda x: (x[1]), reverse=True)

   # app = wx.App()
   # main_win = CoMatrixView(None)
   # main_win.renderMatrix(degrees, groups)
   # main_win.Show()
   # app.MainLoop()

   # if __name__ == '__main__':
