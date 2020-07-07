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
from core.cnki_parser import *
###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_splitter3 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter3.Bind( wx.EVT_IDLE, self.m_splitter3OnIdle )

		self.m_panel2 = wx.Panel( self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_MULTIPLE|wx.dataview.DV_ROW_LINES|wx.dataview.DV_SINGLE )
		bSizer7.Add( self.m_dataViewListCtrl1, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer7 )
		self.m_panel2.Layout()
		bSizer7.Fit( self.m_panel2 )
		self.m_panel3 = wx.Panel( self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_dataViewListCtrl2 = wx.dataview.DataViewListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_dataViewListCtrl2, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer8 )
		self.m_panel3.Layout()
		bSizer8.Fit( self.m_panel3 )
		self.m_splitter3.SplitVertically( self.m_panel2, self.m_panel3, 0 )
		bSizer6.Add( self.m_splitter3, 1, wx.EXPAND, 5 )

		self.m_dataViewListCtrl1.AppendTextColumn("Text")
		self.m_dataViewListCtrl1.AppendTextColumn("Text")

		data = ["True", "row 1"]
		self.m_dataViewListCtrl1.AppendItem(data)

		data = ["False", "row 3"]
		self.m_dataViewListCtrl1.AppendItem(data)
		# bSizer1.Add(listctrl, 0, wx.ALL,5)
		self.insertData()
		self.SetSizer( bSizer6 )
		self.Layout()

	def __del__( self ):
		pass

	def m_splitter3OnIdle( self, event ):
		self.m_splitter3.SetSashPosition( 0 )
		self.m_splitter3.Unbind( wx.EVT_IDLE )

	def insertData(self):
		path = "F:\\002-测试数据\\NewNetworkAttack\\input\\CNKI-637293898682050000.xlsx"
		analyzer = SciMetricsAnalyzer('CNKI', path, None)
		analyzer.analyze_authors()
		for key, value in analyzer.first_authors.items():
			data = [key, str(value.article_count)]
			self.m_dataViewListCtrl1.AppendItem(data)

