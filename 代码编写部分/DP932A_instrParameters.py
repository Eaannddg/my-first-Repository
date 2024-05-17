import wx
import pyvisa
from DP932A_INSTR import DP932A_Controller
import powerPanel

class PowerSupplyInstrParameters(wx.Panel):
    name = 'Power Supply Controller'

    def __init__(self, parent, connectPanel,**kwargs):
        super(PowerSupplyInstrParameters, self).__init__(parent)
        self.connectPanel = connectPanel
        self.visaAddrLst = kwargs['visaAddrLst']
        self.DP932A_controller = None  # 初始化控制器实例
        self.InitUI()

    def InitUI(self):
        sb = wx.StaticBox(self, label='DP932A Parameters');
        vbox = wx.StaticBoxSizer(sb, wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # 连接部分
        self.connectionBox = wx.BoxSizer(wx.HORIZONTAL)
        self.title1 = wx.StaticText(self, label='连接设置:')
        self.connectionLabel = wx.StaticText(self, label='GPIB地址')
        self.connectionInput = wx.ComboBox(self, choices=self.visaAddrLst)
        self.connectionBox.AddMany([
            (self.title1, 0, wx.EXPAND),
            (self.connectionLabel, 0, wx.EXPAND),
            (self.connectionInput, 1, wx.EXPAND),
        ])
        connectbox =wx.BoxSizer(wx.HORIZONTAL)
        self.connectBtn = wx.Button(self, label='连接')
        self.disconnectBtn = wx.Button(self, label='断开连接')
        connectbox.AddMany([(self.connectBtn, 0, wx.EXPAND),
                            (self.disconnectBtn, 0, wx.EXPAND)])

        # 事件处理
        self.connectBtn.Bind(wx.EVT_BUTTON, self.connect)
        self.disconnectBtn.Bind(wx.EVT_BUTTON, self.disconnect)

        # 将部分添加到主布局管理器
        hbox.AddMany([
            (self.connectionBox, 0, wx.EXPAND),
        ])
        vbox.AddMany([(hbox,0,wx.EXPAND),(connectbox,0)])

        self.SetSizer(vbox)

    def connect(self, event):
        address = self.connectionInput.GetValue()
        self.DP932A_controller = DP932A_Controller(address)
        self.DP932A_controller.panelClass = powerPanel.DP932A_ControllerPanel
        self.connectPanel.instList.append(self.DP932A_controller)

    def disconnect(self, event):
        if self.DP932A_controller:
            self.DP932A_controller.disconnect()
            if self.DP932A_controller in self.connectPanel.instList:
                self.connectPanel.instList.remove(self.DP932A_controller)




