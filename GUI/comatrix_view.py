# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class CoMatrixView
###########################################################################


import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import \
FigureCanvasWxAgg as FigCanvas, \
NavigationToolbar2WxAgg as NavigationToolbar


import synonyms
class CoMatrixView ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1024,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )

		self.m_panel1 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_dataViewListCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		self.m_panel2 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		# bSizer3 = wx.BoxSizer( wx.VERTICAL )
		#
		#
		# self.m_panel2.SetSizer( bSizer3 )
		# self.m_panel2.Layout()
		# bSizer3.Fit( self.m_panel2 )
		self.m_splitter1.SplitVertically( self.m_panel1, self.m_panel2, 292 )
		bSizer1.Add( self.m_splitter1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )
		# Connect Events
		self.m_dataViewListCtrl1.Bind(wx.dataview.EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.test, id=wx.ID_ANY)
		self.__initUI__()


	def __initUI__(self):
		self.m_dataViewListCtrl1.AppendToggleColumn('Visible')
		self.m_dataViewListCtrl1.AppendTextColumn('Term')
		self.m_dataViewListCtrl1.AppendTextColumn('Freq')


	def __del__( self ):
		pass

	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 292 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )

	# Virtual event handlers, overide them in your derived class
	def test(self, event):
		print('ok')
		values = self.m_dataViewListCtrl1.GetStore()
		print('pause')

	def analyze(self, data):
		index=0
		result = {}
		for item in data:
			tomerge = item[0]
			index+=1
			result[tomerge] = 1
			for others in data[index:]:
				to_cmp = others[0]
				score = synonyms.compare(tomerge, to_cmp, seg=True)
				if score > 0.5:
					result[tomerge] += 1
					print('{}-{}-{}'.format(tomerge, to_cmp, score))
	def renderMatrix(self, data, groups):
		for item in data:
			row = [True, item[0], str(item[1])]
			self.m_dataViewListCtrl1.AppendItem(row)
		matplotlib.rcParams['font.sans-serif'] = ['SimHei']
		matplotlib.rcParams['font.family']='sans-serif'
		fig = plt.figure()
		canvas = FigCanvas(self.m_panel2, -1, fig)
		g = nx.Graph()
		# g.add_node('王豫')
		index = 0
		for key in groups.keys():
			# if index > 8:
			# 	break
			author_list = key.split(',')
			g.add_edge(author_list[0], author_list[1])
			index+=1

		pos = nx.spring_layout(g,k=0.15,iterations=20)
		# edge_labels = dict([((u, v,), g.get_edge_data(u, v)['0']) for u, v in g.edges])
		# nx.draw_networkx_nodes(g, pos)
		# nx.draw_networkx_labels(g, pos, labels, font_size=8)
		# nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
		nx.draw(g, pos, with_labels=True)
		nodes = g.nodes()
		# plt.figure(3, figsize=(30, 30))
		# nx.draw(g, with_labels=True)
		# nx.draw(g, with_labels=True)
		self.vbox = wx.BoxSizer(wx.VERTICAL)
		self.vbox.Add(canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
		self.toolbar = NavigationToolbar(canvas)
		self.vbox.Add(self.toolbar, 0, wx.EXPAND)
		self.m_panel2.SetSizer(self.vbox)
		self.vbox.Fit(self)

