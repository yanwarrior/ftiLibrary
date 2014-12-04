#Boa:Frame:Frame1

import wx
import wx.lib.buttons

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GENBITMAPTOGGLEBUTTON1, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICLINE1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, 
 wxID_FRAME1STATICTEXT9, 
] = [wx.NewId() for _init_ctrls in range(13)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(412, 164), size=wx.Size(526, 350),
              style=wx.DEFAULT_FRAME_STYLE, title=u'About  FTI - Library')
        self.SetClientSize(wx.Size(510, 312))
        self.SetIcon(wx.Icon(u'img/Custom-Icon-Design-Flatastic-5-Library.ico',
              wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(510, 312),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'FTI - Library ', name='staticText1', parent=self.panel1,
              pos=wx.Point(200, 32), size=wx.Size(190, 42), style=0)
        self.staticText1.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tempus Sans ITC'))
        self.staticText1.SetForegroundColour(wx.Colour(0, 128, 128))

        self.genBitmapToggleButton1 = wx.lib.buttons.GenBitmapToggleButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTOGGLEBUTTON1,
              name='genBitmapToggleButton1', parent=self.panel1,
              pos=wx.Point(24, 40), size=wx.Size(152, 144),
              style=wx.NO_3D | wx.NO_BORDER)
        self.genBitmapToggleButton1.SetBitmapDisabled(wx.Bitmap(u'img/library-icon.png',
              wx.BITMAP_TYPE_PNG))
        self.genBitmapToggleButton1.Enable(False)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Versi 0.0.1', name='staticText2', parent=self.panel1,
              pos=wx.Point(200, 72), size=wx.Size(70, 18), style=0)
        self.staticText2.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.staticText2.SetForegroundColour(wx.Colour(128, 128, 128))

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'pencarian buku pemrograman lengkap (versi inggris) dilangkapi dengan index pencarian dari judul buku yang akan anda cari. fitur download memungkinkan anda untuk mengunduh buku-buku yang anda minati. dan buku2 ini bersifat "gratis" dengan halaman per bukunya bisa lebih dari 100 halaman. apapun tentang pemrograman.',
              name='staticText3', parent=self.panel1, pos=wx.Point(200, 96),
              size=wx.Size(296, 96), style=wx.NO_FULL_REPAINT_ON_RESIZE)
        self.staticText3.SetForegroundColour(wx.Colour(128, 128, 128))

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'API Information', name='staticText4', parent=self.panel1,
              pos=wx.Point(24, 200), size=wx.Size(104, 18), style=0)
        self.staticText4.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Resource URL\t   \nhttp://it-ebooks-api.info/v1/\n',
              name='staticText5', parent=self.panel1, pos=wx.Point(24, 232),
              size=wx.Size(137, 39), style=wx.CLIP_CHILDREN)
        self.staticText5.SetForegroundColour(wx.Colour(0, 0, 255))

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'Request Method\t  \nREST (GET)\n', name='staticText6',
              parent=self.panel1, pos=wx.Point(176, 232), size=wx.Size(97, 39),
              style=0)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Response Format\nJSON', name='staticText7',
              parent=self.panel1, pos=wx.Point(288, 232), size=wx.Size(85, 26),
              style=wx.CLIP_CHILDREN)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'Response Encoding\nUTF-8', name='staticText8',
              parent=self.panel1, pos=wx.Point(392, 232), size=wx.Size(94, 26),
              style=wx.CLIP_CHILDREN)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(24, 224),
              size=wx.Size(464, 2), style=0)

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Coder By : Pythonizam', name='staticText9',
              parent=self.panel1, pos=wx.Point(24, 288), size=wx.Size(110, 13),
              style=0)
        self.staticText9.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))
        self.staticText9.SetForegroundColour(wx.Colour(176, 176, 176))

    def __init__(self, parent):
        self._init_ctrls(parent)
