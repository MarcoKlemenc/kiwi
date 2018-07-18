import wx
from kiwi import Kiwi
  
class Mywin(wx.Frame): 
    def __init__(self, parent, title): 
        super(Mywin, self).__init__(parent, title = title,size = (800,600))
          
        panel = wx.Panel(self) 
        vbox = wx.BoxSizer(wx.VERTICAL) 
            
        hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
        l1 = wx.StaticText(panel, -1, "From") 
          
        hbox1.Add(l1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.t1 = wx.TextCtrl(panel) 
          
        hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.t1.Bind(wx.EVT_TEXT,self.OnKeyTyped) 
        vbox.Add(hbox1) 
          
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        l2 = wx.StaticText(panel, -1, "Mode") 
          
        hbox2.Add(l2, 1, wx.ALIGN_LEFT|wx.ALL,5)
        self.t2 = wx.TextCtrl(panel)
        self.t1.SetMaxLength(3)
          
        hbox2.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        vbox.Add(hbox2) 
        self.t2.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)
          
        hbox3 = wx.BoxSizer(wx.HORIZONTAL) 
        l3 = wx.StaticText(panel, -1, "Max price") 
          
        hbox3.Add(l3,1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.t3 = wx.TextCtrl(panel) 
          
        hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        vbox.Add(hbox3) 

        hbox4 = wx.BoxSizer(wx.HORIZONTAL) 
        l4 = wx.StaticText(panel, -1, "Max stopovers") 
          
        hbox4.Add(l4,1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.t4 = wx.TextCtrl(panel,size = (200,100),style = wx.TE_MULTILINE) 
          
        hbox4.Add(self.t4,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        vbox.Add(hbox4) 
        self.t4.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressed)  

        hbox5 = wx.BoxSizer(wx.HORIZONTAL) 
        l5 = wx.StaticText(panel, -1, "Results") 
          
        hbox5.Add(l5,1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.t5 = wx.TextCtrl(panel,size = (500,300),style = wx.TE_MULTILINE|wx.TE_READONLY) 
          
        hbox5.Add(self.t5,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        vbox.Add(hbox5) 

        panel.SetSizer(vbox) 
          
        self.Centre() 
        self.Show() 
        self.Fit()  
          
    def OnKeyTyped(self, event): 
        print (event.GetString())
          
    def OnEnterPressed(self,event): 
        print ("A")
        a = Kiwi(self.t2.GetValue(), self.t1.GetValue(), self.t3.GetValue(), self.t4.GetValue())
        self.t5.SetValue("\n".join("{}\t{}\t{}\t{}, {}".format(k[0], v[0], int(v[1]), k[1], k[2]) for k, v in a.execute().items()))
          
    def OnMaxLen(self,event): 
        print ("Maximum length reached")
          
app = wx.App() 
Mywin(None,  'Kiwi')
app.MainLoop()
