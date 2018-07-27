import wx
from kiwi import Kiwi

class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title = title,size = (800,600))
        
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(6, 5)

        l1 = wx.StaticText(panel, -1, "From")
        sizer.Add(l1, pos=(1, 1), span=(1, 1), flag=wx.EXPAND)

        self.t1 = wx.TextCtrl(panel)
        sizer.Add(self.t1, pos=(1, 2), span=(1, 1), flag=wx.EXPAND)
        self.t1.Bind(wx.EVT_TEXT,self.OnKeyTyped)
        self.t1.SetMaxLength(3)
        self.t1.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)
        
        l2 = wx.StaticText(panel, -1, "Mode")
        sizer.Add(l2, pos=(2, 1), span=(1, 1), flag=wx.EXPAND)
        
        self.t2 = wx.TextCtrl(panel)
        sizer.Add(self.t2, pos=(2, 2), span=(1, 1), flag=wx.EXPAND)

        l3 = wx.StaticText(panel, -1, "Max price")
        sizer.Add(l3, pos=(3, 1), span=(1, 1), flag=wx.EXPAND)

        self.t3 = wx.TextCtrl(panel)
        sizer.Add(self.t3, pos=(3, 2), span=(1, 1), flag=wx.EXPAND)

        l4 = wx.StaticText(panel, -1, "Max stopovers")
        sizer.Add(l4, pos=(4, 1), span=(1, 1), flag=wx.EXPAND)

        self.t4 = wx.TextCtrl(panel)
        sizer.Add(self.t4, pos=(4, 2), span=(1, 1), flag=wx.EXPAND)

        self.t5 = wx.TextCtrl(panel, size=(525,500), style=wx.TE_MULTILINE|wx.TE_READONLY)
        sizer.Add(self.t5, pos=(1, 4), span=(6, 1), flag=wx.EXPAND)

        self.t6 = wx.Button(panel, -1, "Search")
        sizer.Add(self.t6, pos=(5, 1), span=(1, 2), flag=wx.EXPAND)
        self.t6.Bind(wx.EVT_BUTTON,self.OnClicked)

        panel.SetSizerAndFit(sizer)
        self.Center()
        self.Show()
        
    def OnKeyTyped(self, event):
        print (event.GetString())
        
    def OnClicked(self,event):
        kiwi = Kiwi(self.t2.GetValue(), self.t1.GetValue(), self.t3.GetValue(), self.t4.GetValue())
        data = kiwi.execute().items()
        self.t5.SetValue("\n".join("{}\t{}\t{}\t{}, {}".format(k[0], v[0], int(v[1]), k[1], k[2]) for k, v in data))
        
    def OnMaxLen(self,event):
        print ("Maximum length reached")
        
app = wx.App()
Mywin(None, 'Kiwi')
app.MainLoop()
