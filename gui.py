import wx

from GUI.listview import *
from GUI.main_windows import *
if __name__ == '__main__':
   # 下面是使用wxPython的固定用法
    app = wx.App()
    main_win = MainWindow(None)
    main_win.Show()
    app.MainLoop()