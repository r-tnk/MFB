# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 23 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ModEM File Builder v2.1", pos = wx.DefaultPosition, size = wx.Size( 927,678 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 13, 70, 90, 90, False, "Lucida Grande" ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer3.Add( self.m_dirPicker1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook2.SetFont( wx.Font( 13, 70, 90, 90, False, "Lucida Grande" ) )
		
		self.xset1 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel27 = wx.Panel( self.xset1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel111 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel111, wx.ID_ANY, u"X(EW)" ), wx.VERTICAL )
		
		self.m_staticText21412 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Maximum Length [m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21412.Wrap( -1 )
		sbSizer31.Add( self.m_staticText21412, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.XL = wx.TextCtrl( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer31.Add( self.XL, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText61312 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Size [m], Number [blocks]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61312.Wrap( -1 )
		sbSizer31.Add( self.m_staticText61312, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.XGrid = wx.TextCtrl( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE )
		sbSizer31.Add( self.XGrid, 5, wx.ALL|wx.EXPAND, 5 )
		
		self.SETX = wx.Button( sbSizer31.GetStaticBox(), wx.ID_ANY, u"SET X", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer31.Add( self.SETX, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel111.SetSizer( sbSizer31 )
		self.m_panel111.Layout()
		sbSizer31.Fit( self.m_panel111 )
		bSizer18.Add( self.m_panel111, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel121 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel121, wx.ID_ANY, u"Y(NS)" ), wx.VERTICAL )
		
		self.m_staticText214112 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Maximum Length [m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText214112.Wrap( -1 )
		sbSizer11.Add( self.m_staticText214112, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.YL = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer11.Add( self.YL, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText613113 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Size [m], Number [blocks]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText613113.Wrap( -1 )
		sbSizer11.Add( self.m_staticText613113, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.YGrid = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE )
		sbSizer11.Add( self.YGrid, 5, wx.ALL|wx.EXPAND, 5 )
		
		self.SETY = wx.Button( sbSizer11.GetStaticBox(), wx.ID_ANY, u"SET Y", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer11.Add( self.SETY, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel121.SetSizer( sbSizer11 )
		self.m_panel121.Layout()
		sbSizer11.Fit( self.m_panel121 )
		bSizer18.Add( self.m_panel121, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel131 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer51 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel131, wx.ID_ANY, u"Z(UD)" ), wx.VERTICAL )
		
		self.m_staticText2141112 = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Maximum Length [m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2141112.Wrap( -1 )
		sbSizer51.Add( self.m_staticText2141112, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.ZL = wx.TextCtrl( sbSizer51.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer51.Add( self.ZL, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6131111 = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Size [m], Number [blocks]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6131111.Wrap( -1 )
		sbSizer51.Add( self.m_staticText6131111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.ZGrid = wx.TextCtrl( sbSizer51.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE )
		sbSizer51.Add( self.ZGrid, 5, wx.ALL|wx.EXPAND, 5 )
		
		self.SETZ = wx.Button( sbSizer51.GetStaticBox(), wx.ID_ANY, u"SET Z", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer51.Add( self.SETZ, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel131.SetSizer( sbSizer51 )
		self.m_panel131.Layout()
		sbSizer51.Fit( self.m_panel131 )
		bSizer18.Add( self.m_panel131, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel151 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel151, wx.ID_ANY, u"Example" ), wx.VERTICAL )
		
		self.m_staticText21411111 = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Maximum Length [m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21411111.Wrap( -1 )
		sbSizer61.Add( self.m_staticText21411111, 0, wx.ALL, 5 )
		
		self.m_staticText442 = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"10000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText442.Wrap( -1 )
		self.m_staticText442.SetFont( wx.Font( 13, 70, 90, 90, False, "Lucida Grande" ) )
		self.m_staticText442.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		sbSizer61.Add( self.m_staticText442, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6131121 = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Size [m], Number [blocks]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6131121.Wrap( -1 )
		sbSizer61.Add( self.m_staticText6131121, 0, wx.ALL, 5 )
		
		self.m_staticText4411 = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"10 25\n10 40\n10 60\n\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4411.Wrap( -1 )
		self.m_staticText4411.SetFont( wx.Font( 13, 70, 90, 90, False, "Lucida Grande" ) )
		self.m_staticText4411.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		sbSizer61.Add( self.m_staticText4411, 4, wx.ALL|wx.EXPAND, 5 )
		
		self.SETEX = wx.Button( sbSizer61.GetStaticBox(), wx.ID_ANY, u"SET EX", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer61.Add( self.SETEX, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel151.SetSizer( sbSizer61 )
		self.m_panel151.Layout()
		sbSizer61.Fit( self.m_panel151 )
		bSizer18.Add( self.m_panel151, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel27.SetSizer( bSizer18 )
		self.m_panel27.Layout()
		bSizer18.Fit( self.m_panel27 )
		bSizer17.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel28 = wx.Panel( self.xset1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel33 = wx.Panel( self.m_panel28, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel33, wx.ID_ANY, u"Observation Point" ), wx.VERTICAL )
		
		self.m_staticText131 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Chose center of rectangular", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		sbSizer23.Add( self.m_staticText131, 0, wx.ALIGN_CENTER|wx.ALL, 0 )
		
		m_comboBox11Choices = [ u"33.0 120.50 （1系　長崎・鹿児島の一部）", u"33.0 131.00 （2系　福岡・佐賀・熊本・大分・宮崎・鹿児島）", u"36.0 132.17 （3系　山口・島根・広島）", u"33.0 133.50 （4系　香川・愛媛・徳島・高知）", u"36.0 134.33 （5系　兵庫・鳥取・岡山）", u"36.0 136.00 （6系　京都・大阪・福井・滋賀・三重・奈良・和歌山）", u"36.0 137.17 （7系　石川・富山・岐阜・愛知）", u"36.0 138.50 （8系　新潟・長野・山梨・静岡）", u"36.0 139.83 （9系　東京・福島・栃木・茨城・埼玉・千葉・群馬・神奈川）", u"40.0 140.83 （10系　青森・秋田・山形・岩手・宮城）", u"44.0 140.25 （11系　道南）", u"44.0 142.25 （12系　道央）", u"44.0 144.25 （13系　道東）", u"26.0 142.00 （14系　東京小笠原）", u"26.0 127.50 （15系　沖縄本島）", u"26.0 124.00 （16系　沖縄離島西部）", u"26.0 131.00 （17系　沖縄離島東部）", u"26.0 136.00 （18系　沖ノ鳥島）", u"26.0 154.00 （19系　南鳥島）" ]
		self.m_comboBox11 = wx.ComboBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Chose center of rectangular", wx.DefaultPosition, wx.DefaultSize, m_comboBox11Choices, wx.CB_READONLY )
		sbSizer23.Add( self.m_comboBox11, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2121 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Enter Center Point (lat, lon [ddd.dddd])", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2121.Wrap( -1 )
		sbSizer23.Add( self.m_staticText2121, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Center = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer23.Add( self.Center, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6121 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Observation point (lat, lon [ddd.dddd])", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6121.Wrap( -1 )
		sbSizer23.Add( self.m_staticText6121, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Obs = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE )
		sbSizer23.Add( self.Obs, 5, wx.ALL|wx.EXPAND, 5 )
		
		self.SETPOINTS = wx.Button( sbSizer23.GetStaticBox(), wx.ID_ANY, u"SET Points", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer23.Add( self.SETPOINTS, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel33.SetSizer( sbSizer23 )
		self.m_panel33.Layout()
		sbSizer23.Fit( self.m_panel33 )
		bSizer19.Add( self.m_panel33, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel34 = wx.Panel( self.m_panel28, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer24 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel34, wx.ID_ANY, u"Draw grid and points" ), wx.VERTICAL )
		
		self.m_panel45 = wx.Panel( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer24.Add( self.m_panel45, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.ADrawfrid = wx.Button( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Auto Draw", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer24.Add( self.ADrawfrid, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel46 = wx.Panel( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer24.Add( self.m_panel46, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText112 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Range Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText112.Wrap( -1 )
		sbSizer24.Add( self.m_staticText112, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer2 = wx.GridSizer( 4, 2, 0, 0 )
		
		self.m_staticText100 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"X Min [m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText100.Wrap( -1 )
		gSizer2.Add( self.m_staticText100, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText1001 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"X Max [m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1001.Wrap( -1 )
		gSizer2.Add( self.m_staticText1001, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.XminG = wx.TextCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.XminG, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.XMaxG = wx.TextCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.XMaxG, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText1002 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Y Min [m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1002.Wrap( -1 )
		gSizer2.Add( self.m_staticText1002, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText1003 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Y Max [m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1003.Wrap( -1 )
		gSizer2.Add( self.m_staticText1003, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.YminG = wx.TextCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.YminG, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.YMaxG = wx.TextCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.YMaxG, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer24.Add( gSizer2, 0, wx.EXPAND, 5 )
		
		self.DrawGrid = wx.Button( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Draw", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer24.Add( self.DrawGrid, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel34.SetSizer( sbSizer24 )
		self.m_panel34.Layout()
		sbSizer24.Fit( self.m_panel34 )
		bSizer19.Add( self.m_panel34, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel28.SetSizer( bSizer19 )
		self.m_panel28.Layout()
		bSizer19.Fit( self.m_panel28 )
		bSizer17.Add( self.m_panel28, 2, wx.EXPAND |wx.ALL, 5 )
		
		
		self.xset1.SetSizer( bSizer17 )
		self.xset1.Layout()
		bSizer17.Fit( self.xset1 )
		self.m_notebook2.AddPage( self.xset1, u"GridSet", False )
		self.m_panel6 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer21 = wx.GridSizer( 2, 2, 0, 0 )
		
		sbSizer111 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel6, wx.ID_ANY, u"1. Set topography" ), wx.VERTICAL )
		
		self.m_panel43 = wx.Panel( sbSizer111.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer111.Add( self.m_panel43, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SETTopo = wx.Button( sbSizer111.GetStaticBox(), wx.ID_ANY, u"SET Topo", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer111.Add( self.SETTopo, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel44 = wx.Panel( sbSizer111.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer111.Add( self.m_panel44, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		gSizer21.Add( sbSizer111, 1, wx.EXPAND, 5 )
		
		self.m_panel12 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel12, wx.ID_ANY, u"2. Set parameters and Create files" ), wx.VERTICAL )
		
		self.m_panel1611 = wx.Panel( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer911 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2111 = wx.StaticText( self.m_panel1611, wx.ID_ANY, u"Smoothing Parameter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2111.Wrap( -1 )
		bSizer911.Add( self.m_staticText2111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.Spara = wx.TextCtrl( self.m_panel1611, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer911.Add( self.Spara, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.SparaSet = wx.Button( self.m_panel1611, wx.ID_ANY, u"SET", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer911.Add( self.SparaSet, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel1611.SetSizer( bSizer911 )
		self.m_panel1611.Layout()
		bSizer911.Fit( self.m_panel1611 )
		sbSizer14.Add( self.m_panel1611, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel1711 = wx.Panel( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1011 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2211 = wx.StaticText( self.m_panel1711, wx.ID_ANY, u"Initial resistivity value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2211.Wrap( -1 )
		bSizer1011.Add( self.m_staticText2211, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.IRV = wx.TextCtrl( self.m_panel1711, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1011.Add( self.IRV, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button1611 = wx.Button( self.m_panel1711, wx.ID_ANY, u"SET", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1011.Add( self.m_button1611, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.m_panel1711.SetSizer( bSizer1011 )
		self.m_panel1711.Layout()
		bSizer1011.Fit( self.m_panel1711 )
		sbSizer14.Add( self.m_panel1711, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel1811 = wx.Panel( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1111 = wx.BoxSizer( wx.VERTICAL )
		
		self.CreateFIles = wx.Button( self.m_panel1811, wx.ID_ANY, u"Create model.ws and topo.cov", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1111.Add( self.CreateFIles, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		self.m_panel1811.SetSizer( bSizer1111 )
		self.m_panel1811.Layout()
		bSizer1111.Fit( self.m_panel1811 )
		sbSizer14.Add( self.m_panel1811, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel12.SetSizer( sbSizer14 )
		self.m_panel12.Layout()
		sbSizer14.Fit( self.m_panel12 )
		gSizer21.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel13 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer241 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel13, wx.ID_ANY, u"3. Check the model with 3D figure" ), wx.VERTICAL )
		
		self.m_panel54 = wx.Panel( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer241.Add( self.m_panel54, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.ADraw3D = wx.Button( sbSizer241.GetStaticBox(), wx.ID_ANY, u"Auto Draw", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer241.Add( self.ADraw3D, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel55 = wx.Panel( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer241.Add( self.m_panel55, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText1121 = wx.StaticText( sbSizer241.GetStaticBox(), wx.ID_ANY, u"Range and GMT Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1121.Wrap( -1 )
		sbSizer241.Add( self.m_staticText1121, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer22 = wx.GridSizer( 4, 4, 0, 0 )
		
		self.m_staticText1004 = wx.StaticText( sbSizer241.GetStaticBox(), wx.ID_ANY, u"X Min [m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1004.Wrap( -1 )
		gSizer22.Add( self.m_staticText1004, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.XMin3D = wx.TextCtrl( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.XMin3D, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText10011 = wx.StaticText( sbSizer241.GetStaticBox(), wx.ID_ANY, u"X Max [m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10011.Wrap( -1 )
		gSizer22.Add( self.m_staticText10011, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.XMax3D = wx.TextCtrl( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.XMax3D, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText10021 = wx.StaticText( sbSizer241.GetStaticBox(), wx.ID_ANY, u"Y Min [m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10021.Wrap( -1 )
		gSizer22.Add( self.m_staticText10021, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.YMin3D = wx.TextCtrl( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.YMin3D, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText10031 = wx.StaticText( sbSizer241.GetStaticBox(), wx.ID_ANY, u"Y Max [m]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10031.Wrap( -1 )
		gSizer22.Add( self.m_staticText10031, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.YMax3D = wx.TextCtrl( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.YMax3D, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText47 = wx.StaticText( sbSizer241.GetStaticBox(), wx.ID_ANY, u"Scale", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		gSizer22.Add( self.m_staticText47, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SCSET = wx.TextCtrl( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.SCSET, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticText48 = wx.StaticText( sbSizer241.GetStaticBox(), wx.ID_ANY, u"Azimuth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		gSizer22.Add( self.m_staticText48, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.AZSET = wx.TextCtrl( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.AZSET, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText50 = wx.StaticText( sbSizer241.GetStaticBox(), wx.ID_ANY, u"Elevation angel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		gSizer22.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.ELSET = wx.TextCtrl( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.ELSET, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer241.Add( gSizer22, 0, wx.EXPAND, 5 )
		
		self.Draw3DM = wx.Button( sbSizer241.GetStaticBox(), wx.ID_ANY, u"Draw", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer241.Add( self.Draw3DM, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel56 = wx.Panel( sbSizer241.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer241.Add( self.m_panel56, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel13.SetSizer( sbSizer241 )
		self.m_panel13.Layout()
		sbSizer241.Fit( self.m_panel13 )
		gSizer21.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel37 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel37, wx.ID_ANY, u"4. Finish!" ), wx.VERTICAL )
		
		self.m_panel41 = wx.Panel( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer15.Add( self.m_panel41, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.Done = wx.Button( sbSizer15.GetStaticBox(), wx.ID_ANY, u"Done!", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer15.Add( self.Done, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel42 = wx.Panel( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer15.Add( self.m_panel42, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel37.SetSizer( sbSizer15 )
		self.m_panel37.Layout()
		sbSizer15.Fit( self.m_panel37 )
		gSizer21.Add( self.m_panel37, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel6.SetSizer( gSizer21 )
		self.m_panel6.Layout()
		gSizer21.Fit( self.m_panel6 )
		self.m_notebook2.AddPage( self.m_panel6, u"Create", False )
		
		bSizer3.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_dirPicker1.Bind( wx.EVT_DIRPICKER_CHANGED, self.BrowsOnDirChanged )
		self.SETX.Bind( wx.EVT_BUTTON, self.SETXOnButtonClick )
		self.SETY.Bind( wx.EVT_BUTTON, self.SETYOnButtonClick )
		self.SETZ.Bind( wx.EVT_BUTTON, self.SETZOnButtonClick )
		self.SETEX.Bind( wx.EVT_BUTTON, self.SETEXOnButtonClick )
		self.SETPOINTS.Bind( wx.EVT_BUTTON, self.SETPOINTSOnButtonClick )
		self.ADrawfrid.Bind( wx.EVT_BUTTON, self.ADrawONButtonClick )
		self.DrawGrid.Bind( wx.EVT_BUTTON, self.DrawGridOnClick )
		self.SETTopo.Bind( wx.EVT_BUTTON, self.TopoOnClick )
		self.SparaSet.Bind( wx.EVT_BUTTON, self.SparasetOnclick )
		self.m_button1611.Bind( wx.EVT_BUTTON, self.IRVOnClick )
		self.CreateFIles.Bind( wx.EVT_BUTTON, self.CreateFIlesOnVlick )
		self.ADraw3D.Bind( wx.EVT_BUTTON, self.ADraw3DOnClick )
		self.Draw3DM.Bind( wx.EVT_BUTTON, self.Draw3DOnClick )
		self.Done.Bind( wx.EVT_BUTTON, self.DoneOnClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def BrowsOnDirChanged( self, event ):
		event.Skip()
	
	def SETXOnButtonClick( self, event ):
		event.Skip()
	
	def SETYOnButtonClick( self, event ):
		event.Skip()
	
	def SETZOnButtonClick( self, event ):
		event.Skip()
	
	def SETEXOnButtonClick( self, event ):
		event.Skip()
	
	def SETPOINTSOnButtonClick( self, event ):
		event.Skip()
	
	def ADrawONButtonClick( self, event ):
		event.Skip()
	
	def DrawGridOnClick( self, event ):
		event.Skip()
	
	def TopoOnClick( self, event ):
		event.Skip()
	
	def SparasetOnclick( self, event ):
		event.Skip()
	
	def IRVOnClick( self, event ):
		event.Skip()
	
	def CreateFIlesOnVlick( self, event ):
		event.Skip()
	
	def ADraw3DOnClick( self, event ):
		event.Skip()
	
	def Draw3DOnClick( self, event ):
		event.Skip()
	
	def DoneOnClick( self, event ):
		event.Skip()
	

