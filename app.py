import wx
from kiwi import Kiwi
from datetime import date

class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title = title,size = (800,600))
        
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(10, 5)

        from_label = wx.StaticText(panel, -1, "From")
        sizer.Add(from_label, pos=(1, 1), span=(1, 1), flag=wx.EXPAND)

        self.from_field = wx.TextCtrl(panel)
        sizer.Add(self.from_field, pos=(1, 2), span=(1, 1), flag=wx.EXPAND)
        self.from_field.SetMaxLength(3)
        
        mode_label = wx.StaticText(panel, -1, "Mode")
        sizer.Add(mode_label, pos=(2, 1), span=(1, 1), flag=wx.EXPAND)
        
        self.mode_field = wx.TextCtrl(panel)
        sizer.Add(self.mode_field, pos=(2, 2), span=(1, 1), flag=wx.EXPAND)

        max_price_label = wx.StaticText(panel, -1, "Max price")
        sizer.Add(max_price_label, pos=(3, 1), span=(1, 1), flag=wx.EXPAND)

        self.max_price_field = wx.TextCtrl(panel)
        sizer.Add(self.max_price_field, pos=(3, 2), span=(1, 1), flag=wx.EXPAND)

        max_stopovers_label = wx.StaticText(panel, -1, "Max stopovers")
        sizer.Add(max_stopovers_label, pos=(4, 1), span=(1, 1), flag=wx.EXPAND)

        self.max_stopovers_field = wx.TextCtrl(panel)
        sizer.Add(self.max_stopovers_field, pos=(4, 2), span=(1, 1), flag=wx.EXPAND)

        date_from_label = wx.StaticText(panel, -1, "Date from")
        sizer.Add(date_from_label, pos=(5, 1), span=(1, 1), flag=wx.EXPAND)

        self.date_from_field = wx.TextCtrl(panel)
        sizer.Add(self.date_from_field, pos=(5, 2), span=(1, 1), flag=wx.EXPAND)
        self.date_from_field.SetValue(date.today().strftime("%d/%m/%Y"))

        date_to_label = wx.StaticText(panel, -1, "Date to")
        sizer.Add(date_to_label, pos=(6, 1), span=(1, 1), flag=wx.EXPAND)

        self.date_to_field = wx.TextCtrl(panel)
        sizer.Add(self.date_to_field, pos=(6, 2), span=(1, 1), flag=wx.EXPAND)
        self.date_to_field.SetValue(date.today().strftime("%d/%m/%Y"))

        airlines_label = wx.StaticText(panel, -1, "Airlines")
        sizer.Add(airlines_label, pos=(7, 1), span=(1, 1), flag=wx.EXPAND)

        self.airlines_field = wx.TextCtrl(panel)
        sizer.Add(self.airlines_field, pos=(7, 2), span=(1, 1), flag=wx.EXPAND)

        self.results = wx.TextCtrl(panel, size=(525,475), style=wx.TE_MULTILINE|wx.TE_READONLY)
        sizer.Add(self.results, pos=(1, 4), span=(9, 1), flag=wx.EXPAND)

        self.button = wx.Button(panel, -1, "Search")
        sizer.Add(self.button, pos=(8, 1), span=(1, 2), flag=wx.EXPAND)
        self.button.Bind(wx.EVT_BUTTON,self.OnClicked)

        panel.SetSizerAndFit(sizer)
        self.Center()
        self.Show()
        
    def OnClicked(self,event):
        kiwi = Kiwi(self.mode_field.GetValue(), self.from_field.GetValue(), self.max_price_field.GetValue(), self.max_stopovers_field.GetValue(), self.date_from_field.GetValue(), self.date_to_field.GetValue(), self.airlines_field.GetValue())
        data = kiwi.execute().items()
        self.results.SetValue("\n".join("{}\t{}\t{}\t{}, {}".format(k[0], v[0], int(v[1]), k[1], k[2]) for k, v in data))
        
app = wx.App()
Mywin(None, 'Kiwi')
app.MainLoop()
