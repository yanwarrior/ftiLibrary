#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import FrameBookit

modules ={u'FrameAbout': [0, '', u'FrameAbout.py'],
 u'FrameBookit': [1, 'Main frame of Application', u'FrameBookit.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = FrameBookit.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
