# -*- coding: utf8 -*-
# ---------------------------------------------------------
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Source: http://github.com/JorgeDeLosSantos/wxpython-demos
# License: MIT License
# ---------------------------------------------------------
#
import wx

class WXDemoFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(200,80))
        self.sz = wx.BoxSizer(wx.VERTICAL)
        # Button
        self.boton = wx.Button(self, -1, u"Button", size=(-1,25))
        # Add to sizer
        self.sz.Add(self.boton, 0, wx.ALIGN_CENTRE|wx.ALL, 10)
        # Bind EVT_BUTTON
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.boton)
        self.SetSizer(self.sz)
        self.Centre(True)
        self.Show()
        
    def OnClick(self,event):
        """
        Method that handle button event
        """
        msg = u"Button pressed"
        title = u"wxButton Demo"
        wx.MessageBox(msg, caption=title)

if __name__=='__main__':
    app = wx.App()
    frame = WXDemoFrame(None, u"wxButton Demo")
    app.MainLoop()
