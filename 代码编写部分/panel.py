import wx
from panel1 import MyPanel1
from panel2 import MyPanel2
from panel3 import MyPanel3


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.notebook = wx.Notebook(self)

        self.panel1 = MyPanel1(self.notebook)
        self.panel2 = MyPanel2(self.notebook)
        self.panel3 = MyPanel3(self.notebook)

        self.notebook.AddPage(self.panel1, "<CH1>通道设置")
        self.notebook.AddPage(self.panel2, "<CH2>通道设置")
        self.notebook.AddPage(self.panel3, "<CH3>通道设置")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.EXPAND)
        self.SetSizer(sizer)


app = wx.App()
frame = wx.Frame(None, title="Panel Switching Example", size=(800, 350))
panel = MyPanel(frame)
frame.Show()
app.MainLoop()
