# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ProjectSettingView
###########################################################################

class ProjectSettingView ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1065,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter5 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter5.Bind( wx.EVT_IDLE, self.m_splitter5OnIdle )

		self.m_panel8 = wx.Panel( self.m_splitter5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer1 = wx.GridBagSizer( 4, 0 )
		gbSizer1.SetFlexibleDirection( wx.VERTICAL )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText8 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gbSizer1.Add( self.m_staticText8, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_dirPicker5 = wx.DirPickerCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gbSizer1.Add( self.m_dirPicker5, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 3 ), wx.EXPAND, 5 )

		self.m_dirPicker6 = wx.DirPickerCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gbSizer1.Add( self.m_dirPicker6, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 3 ), wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gbSizer1.Add( self.m_staticText9, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.m_panel8.SetSizer( gbSizer1 )
		self.m_panel8.Layout()
		gbSizer1.Fit( self.m_panel8 )
		self.m_panel9 = wx.Panel( self.m_splitter5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_treeCtrl1 = wx.TreeCtrl( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		gSizer3.Add( self.m_treeCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel9.SetSizer( gSizer3 )
		self.m_panel9.Layout()
		gSizer3.Fit( self.m_panel9 )
		self.m_splitter5.SplitVertically( self.m_panel8, self.m_panel9, 0 )
		bSizer14.Add( self.m_splitter5, 0, wx.EXPAND, 5 )

		self.m_radioBtn9 = wx.RadioButton( self, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_radioBtn9, 0, wx.ALL, 5 )

		self.m_radioBtn10 = wx.RadioButton( self, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_radioBtn10, 0, wx.ALL, 5 )

		self.m_radioBtn11 = wx.RadioButton( self, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_radioBtn11, 0, wx.ALL, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()

	def __del__( self ):
		pass

	def m_splitter5OnIdle( self, event ):
		self.m_splitter5.SetSashPosition( 0 )
		self.m_splitter5.Unbind( wx.EVT_IDLE )


