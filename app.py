import wx, xlwt
from kiwi import Kiwi
from datetime import date

class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title = title,size = (240,320))
        
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(7, 2)

        from_label = wx.StaticText(panel, -1, "From")
        sizer.Add(from_label, pos=(1, 1), span=(1, 1), flag=wx.EXPAND)

        self.from_field = wx.TextCtrl(panel)
        sizer.Add(self.from_field, pos=(1, 2), span=(1, 1), flag=wx.EXPAND)
        self.from_field.SetMaxLength(3)
        
        max_price_label = wx.StaticText(panel, -1, "Max price")
        sizer.Add(max_price_label, pos=(2, 1), span=(1, 1), flag=wx.EXPAND)

        self.max_price_field = wx.TextCtrl(panel)
        sizer.Add(self.max_price_field, pos=(2, 2), span=(1, 1), flag=wx.EXPAND)

        max_stopovers_label = wx.StaticText(panel, -1, "Max stopovers")
        sizer.Add(max_stopovers_label, pos=(3, 1), span=(1, 1), flag=wx.EXPAND)

        self.max_stopovers_field = wx.TextCtrl(panel)
        sizer.Add(self.max_stopovers_field, pos=(3, 2), span=(1, 1), flag=wx.EXPAND)

        departure_label = wx.StaticText(panel, -1, "Departure")
        sizer.Add(departure_label, pos=(4, 1), span=(1, 1), flag=wx.EXPAND)

        self.departure_field = wx.TextCtrl(panel)
        sizer.Add(self.departure_field, pos=(4, 2), span=(1, 1), flag=wx.EXPAND)
        self.departure_field.SetValue(date.today().strftime("%d/%m/%Y"))

        return_label = wx.StaticText(panel, -1, "Return")
        sizer.Add(return_label, pos=(5, 1), span=(1, 1), flag=wx.EXPAND)

        self.return_field = wx.TextCtrl(panel)
        sizer.Add(self.return_field, pos=(5, 2), span=(1, 1), flag=wx.EXPAND)
        self.return_field.SetValue(date.today().strftime("%d/%m/%Y"))

        airlines_label = wx.StaticText(panel, -1, "Airlines")
        sizer.Add(airlines_label, pos=(6, 1), span=(1, 1), flag=wx.EXPAND)

        self.airlines_field = wx.TextCtrl(panel)
        sizer.Add(self.airlines_field, pos=(6, 2), span=(1, 1), flag=wx.EXPAND)

        self.button = wx.Button(panel, -1, "Search")
        sizer.Add(self.button, pos=(7, 1), span=(1, 2), flag=wx.EXPAND)
        self.button.Bind(wx.EVT_BUTTON,self.OnClicked)

        panel.SetSizerAndFit(sizer)
        self.Center()
        self.Show()
        
    def OnClicked(self,event):
        kiwi = Kiwi(self.from_field.GetValue(), self.max_price_field.GetValue(), self.max_stopovers_field.GetValue(), self.departure_field.GetValue(), self.return_field.GetValue(), self.airlines_field.GetValue())
        data = kiwi.execute()
        wb = xlwt.Workbook()
        ws = wb.add_sheet("Kiwi")
        ws.write(0, 0, "Code")
        ws.write(0, 1, "City")
        ws.write(0, 2, "Country")
        ws.write(0, 3, "Price (one-way)")
        ws.write(0, 4, "Price (roundtrip)")
        ws.write(0, 5, "Distance")
        for i, (k, v) in enumerate(data.items()):
            ws.write(i + 1, 0, k[0])
            ws.write(i + 1, 1, k[1])
            ws.write(i + 1, 2, k[2])
            ws.write(i + 1, 3, v[0])
            ws.write(i + 1, 4, v[1])
            ws.write(i + 1, 5, v[2])
        wb.save("{}.xls".format(self.from_field.GetValue()))
        
app = wx.App()
Mywin(None, 'Kiwi')
app.MainLoop()
