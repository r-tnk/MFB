#! env python
# -*- coding: utf-8 -*-

import os
import sys
import wx
from MEMFBMyFrame2 import MEMFBMyFrame2

if __name__ == '__main__':
    app = wx.App(False)
    frame = MEMFBMyFrame2(None)
    frame.Show(True)
    app.MainLoop()
