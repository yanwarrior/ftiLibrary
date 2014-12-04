#Boa:Frame:Frame1

import wx
import wx.richtext
import wx.html
import modbookit
import webbrowser
import thread
import time
import FrameAbout

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTN_ABOUT, wxID_FRAME1BTN_DOWNLOAD, wxID_FRAME1GG, 
 wxID_FRAME1LBL_ENTER, wxID_FRAME1LBL_HALAMAN, wxID_FRAME1LBL_PROSES, 
 wxID_FRAME1LBL_RESULT, wxID_FRAME1LC_HASIL_PENCARIAN, wxID_FRAME1PANEL1, 
 wxID_FRAME1RICHTEXTCTRL1, wxID_FRAME1SB_HALAMAN, wxID_FRAME1STATICBOX1, 
 wxID_FRAME1STATICBOX2, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1TXT_DETAIL_JUDUL, wxID_FRAME1TXT_DETAIL_PENULIS, 
 wxID_FRAME1TXT_JUDUL_BUKU, 
] = [wx.NewId() for _init_ctrls in range(22)]

class Frame1(wx.Frame):
    def _init_coll_lc_hasil_pencarian_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading=u'No Buku', width=60)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading=u'Judul Buku', width=360)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(308, 163), size=wx.Size(728, 331),
              style=wx.DEFAULT_FRAME_STYLE, title=u'FTI Library - V.0.0.1 ')
        self.SetClientSize(wx.Size(712, 293))
        self.SetIcon(wx.Icon(u'img/Custom-Icon-Design-Flatastic-5-Library.ico',
              wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(712, 293),
              style=wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Pencarian ', name='staticBox1', parent=self.panel1,
              pos=wx.Point(16, 16), size=wx.Size(456, 264), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Detail Buku ', name='staticBox2', parent=self.panel1,
              pos=wx.Point(480, 16), size=wx.Size(216, 264), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Judul Buku', name='staticText1', parent=self.panel1,
              pos=wx.Point(32, 40), size=wx.Size(51, 13), style=0)

        self.txt_judul_buku = wx.TextCtrl(id=wxID_FRAME1TXT_JUDUL_BUKU,
              name=u'txt_judul_buku', parent=self.panel1, pos=wx.Point(32, 56),
              size=wx.Size(424, 21), style=wx.TE_PROCESS_ENTER, value=u'')
        self.txt_judul_buku.Bind(wx.EVT_TEXT_ENTER,
              self.OnTxt_judul_bukuTextEnter, id=wxID_FRAME1TXT_JUDUL_BUKU)
        self.txt_judul_buku.Bind(wx.EVT_KEY_UP, self.OnTxt_judul_bukuKeyUp)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Hasil Pencarian', name='staticText2', parent=self.panel1,
              pos=wx.Point(32, 88), size=wx.Size(73, 13), style=0)

        self.lc_hasil_pencarian = wx.ListCtrl(id=wxID_FRAME1LC_HASIL_PENCARIAN,
              name=u'lc_hasil_pencarian', parent=self.panel1, pos=wx.Point(32,
              104), size=wx.Size(424, 128), style=wx.LC_REPORT)
        self._init_coll_lc_hasil_pencarian_Columns(self.lc_hasil_pencarian)
        self.lc_hasil_pencarian.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnLc_hasil_pencarianListItemSelected,
              id=wxID_FRAME1LC_HASIL_PENCARIAN)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Judul Buku', name='staticText3', parent=self.panel1,
              pos=wx.Point(496, 40), size=wx.Size(51, 13), style=0)

        self.txt_detail_judul = wx.TextCtrl(id=wxID_FRAME1TXT_DETAIL_JUDUL,
              name=u'txt_detail_judul', parent=self.panel1, pos=wx.Point(496,
              56), size=wx.Size(184, 21), style=0, value=u'')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Penulis', name='staticText4', parent=self.panel1,
              pos=wx.Point(496, 88), size=wx.Size(34, 13), style=0)

        self.txt_detail_penulis = wx.TextCtrl(id=wxID_FRAME1TXT_DETAIL_PENULIS,
              name=u'txt_detail_penulis', parent=self.panel1, pos=wx.Point(496,
              104), size=wx.Size(184, 21), style=0, value=u'')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Keterangan ', name='staticText5', parent=self.panel1,
              pos=wx.Point(496, 136), size=wx.Size(60, 13), style=0)

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL1,
              parent=self.panel1, pos=wx.Point(496, 152), size=wx.Size(184, 88),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl1.SetLabel(u'richText')

        self.sb_halaman = wx.SpinButton(id=wxID_FRAME1SB_HALAMAN,
              name=u'sb_halaman', parent=self.panel1, pos=wx.Point(32, 248),
              size=wx.Size(328, 24), style=wx.SP_HORIZONTAL)
        self.sb_halaman.Bind(wx.EVT_SPIN_DOWN, self.OnSb_halamanSpinDown,
              id=wxID_FRAME1SB_HALAMAN)
        self.sb_halaman.Bind(wx.EVT_SPIN_UP, self.OnSb_halamanSpinUp,
              id=wxID_FRAME1SB_HALAMAN)

        self.btn_download = wx.Button(id=wxID_FRAME1BTN_DOWNLOAD,
              label=u'Download', name=u'btn_download', parent=self.panel1,
              pos=wx.Point(552, 248), size=wx.Size(128, 24), style=0)
        self.btn_download.Bind(wx.EVT_BUTTON, self.OnBtn_downloadButton,
              id=wxID_FRAME1BTN_DOWNLOAD)

        self.lbl_halaman = wx.StaticText(id=wxID_FRAME1LBL_HALAMAN,
              label=u'Halaman 1', name=u'lbl_halaman', parent=self.panel1,
              pos=wx.Point(376, 88), size=wx.Size(51, 13), style=0)

        self.lbl_proses = wx.StaticText(id=wxID_FRAME1LBL_PROSES,
              label=u'Proses', name=u'lbl_proses', parent=self.panel1,
              pos=wx.Point(304, 88), size=wx.Size(33, 13), style=0)

        self.lbl_result = wx.StaticText(id=wxID_FRAME1LBL_RESULT,
              label=u'Result 0', name=u'lbl_result', parent=self.panel1,
              pos=wx.Point(208, 88), size=wx.Size(40, 13), style=0)

        self.gg = wx.Gauge(id=wxID_FRAME1GG, name=u'gg', parent=self.panel1,
              pos=wx.Point(376, 248), range=10, size=wx.Size(80, 24),
              style=wx.GA_HORIZONTAL)

        self.lbl_enter = wx.StaticText(id=wxID_FRAME1LBL_ENTER, label=u'',
              name=u'lbl_enter', parent=self.panel1, pos=wx.Point(98, 40),
              size=wx.Size(0, 13), style=0)
        self.lbl_enter.SetForegroundColour(wx.Colour(0, 128, 192))

        self.btn_about = wx.Button(id=wxID_FRAME1BTN_ABOUT, label=u'About',
              name=u'btn_about', parent=self.panel1, pos=wx.Point(496, 248),
              size=wx.Size(48, 24), style=0)
        self.btn_about.Bind(wx.EVT_BUTTON, self.OnBtn_aboutButton,
              id=wxID_FRAME1BTN_ABOUT)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def __cari(self,ex,o):
        self.Disable()
        self.lc_hasil_pencarian.DeleteAllItems()
        
        # cek dulu koneksi
        koneksi = modbookit.checkConnection()
        if koneksi:
            self.query = self.txt_judul_buku.GetValue()
            jsonBook = modbookit.getSearchJson(self.query)
            dataCount = int(jsonBook['Total'])
            try:
                jsonTime = jsonBook['Time']
            except:
                jsonTime = 0.002
            jsonError = jsonBook['Error']
            currentPage = int(jsonBook['Page'])
            rootBook = jsonBook['Books']
            
            # cek error
            if jsonError != 0:
                self.lbl_halaman.SetLabel("Halaman : " +str(self.counter))
                self.lbl_proses.SetLabel(str(jsonTime) + " Detik")
                jumlahBaris = self.lc_hasil_pencarian.GetItemCount()
                self.gg.SetRange(10)
                self.gg.Pulse()
                for i in range(10):
                    
                    time.sleep(0.1)
                    self.gg.SetValue(i)
                    self.lc_hasil_pencarian.InsertStringItem(jumlahBaris,\
                    str(rootBook[i]['ID']))
                    self.lc_hasil_pencarian.SetStringItem(jumlahBaris,1,\
                    str(rootBook[i]['Title']))
                self.gg.SetValue(0)
            else:
                pesan = "Terjadi kesalahan saat request Buku dari server"
                msg = wx.MessageDialog(self,pesan,"Perhatian",wx.ICON_WARNING)
                msg.ShowModal()
                
        else:
            pesan = "Tidak ada koneksi jaringan internet"
            msg = wx.MessageDialog(self,pesan,"Perhatian",wx.ICON_WARNING)
            msg.ShowModal()
        self.Enable()
    
    def upCount(self,ex,o):
        self.Disable()
        try:
            if self.query != "" and self.counter >= 1:
                self.counter = self.counter + 1
                page = str(self.counter)
                jsonData = modbookit.getPageJson(self.query, page)
                self.lbl_halaman.SetLabel("Halaman : " + str(jsonData['Page']))
                self.lbl_proses.SetLabel(str(jsonData['Time']) + " Detik")
                self.lc_hasil_pencarian.DeleteAllItems()
                rootBook = jsonData['Books']
                jumlahBaris = self.lc_hasil_pencarian.GetItemCount()
                self.gg.SetRange(10)
                for i in range(10):
                    time.sleep(0.1)
                    self.gg.SetValue(i)
                    self.lc_hasil_pencarian.InsertStringItem(jumlahBaris,\
                    str(rootBook[i]['ID']))
                    self.lc_hasil_pencarian.SetStringItem(jumlahBaris,1,\
                    str(rootBook[i]['Title']))
                self.gg.SetValue(0)
        except:
            pesan = "Anda Belum melakukan pencarian dengan judul buku"
            msg = wx.MessageDialog(self,pesan,"Perhatian",wx.ICON_WARNING)
            msg.ShowModal()
        self.Enable()
        
    def downCount(self,ex,o):
        self.Disable()
        if self.query != "":
            if self.counter > 1:
                self.counter = self.counter - 1
            page = str(self.counter)
            jsonData = modbookit.getPageJson(self.query, page)
            self.lbl_halaman.SetLabel("Halaman : " + str(self.counter))
            self.lbl_proses.SetLabel(str(jsonData['Time']) + " Detik")
            self.lc_hasil_pencarian.DeleteAllItems()
            rootBook = jsonData['Books']
            jumlahBaris = self.lc_hasil_pencarian.GetItemCount()
            self.gg.SetRange(10)
            for i in range(10):
                time.sleep(0.1)
                self.gg.SetValue(i)
                self.lc_hasil_pencarian.InsertStringItem(jumlahBaris,\
                str(rootBook[i]['ID']))
                self.lc_hasil_pencarian.SetStringItem(jumlahBaris,1,\
                str(rootBook[i]['Title']))
            self.gg.SetValue(0)
        self.Enable()
        '''
        except:
            pesan = "Anda Belum melakukan pencarian dengan judul buku"
            msg = wx.MessageDialog(self,pesan,"Perhatian",wx.ICON_WARNING)
            msg.ShowModal()
        '''


    def OnTxt_judul_bukuTextEnter(self, event):
        self.Disable()
        self.counter = 1
        thread.start_new_thread(self.__cari,("Thread", 1,))
        self.Enable()

    def OnBtn_downloadButton(self, event):
        self.Disable()
        if self.urlDownload:
            webbrowser.open(self.urlDownload)
        else:
            pesan = "Kesalahan Pada Link"
            msg = wx.MessageDialog(self,pesan,"Perhatian",wx.ICON_WARNING)
            msg.ShowModal()
        self.Enable()

    def OnSb_halamanSpinDown(self, event):
        #try:
        thread.start_new_thread(self.downCount, ("Thread", 1,))
        

    def OnSb_halamanSpinUp(self, event):
        thread.start_new_thread(self.upCount, ("Thread", 1,))


    def OnLc_hasil_pencarianListItemSelected(self, event):
        thread.start_new_thread(self.selectDataBook, (" ", event.m_itemIndex, ))
    
    def selectDataBook(self,ex, ev):
        self.Disable()
        noBaris = ev
        try:
            bookId = self.lc_hasil_pencarian.GetItem(noBaris, 0).GetText()
            bookTitle = self.lc_hasil_pencarian.GetItem(noBaris, 1).GetText()
            jsonBookDetail = modbookit.getBookDetailJson(bookId)
            self.txt_detail_judul.SetValue(jsonBookDetail['Title'])
            self.txt_detail_penulis.SetValue(jsonBookDetail['Author'])
            self.richTextCtrl1.SetValue(jsonBookDetail['Description'])
            self.urlDownload = jsonBookDetail['Download']
        except:
            pass
        self.Enable()

    def OnTxt_judul_bukuKeyUp(self, event):
        self.lbl_enter.SetLabel("tekan enter untuk lihat hasil")
        if self.txt_judul_buku.GetValue() == "":
            self.lbl_enter.SetLabel("")

    def OnBtn_aboutButton(self, event):
        about = FrameAbout.create(None)
        about.Show()
        
        
