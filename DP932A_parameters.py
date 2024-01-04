
import wx

class DP932A_InstrParameters(wx.Panel):
    name = 'DP932A Controller'

    def __init__(self, parent, DP932A_controller, **kwargs):
        super(DP932A_InstrParameters, self).__init__(parent)
        self.DP932A_controller = DP932A_controller
        self.InitUI()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 连接设备
        self.connectionBox = wx.BoxSizer(wx.HORIZONTAL)
        self.title1 =wx.StaticText(self,label='连接设备：')
        self.connectionLabel = wx.StaticText(self, label='GPIB Address')
        self.connectionInput = wx.TextCtrl(self)
        self.connectBtn = wx.Button(self, label='Connect')
        self.disconnectBtn = wx.Button(self, label='Disconnect')
        self.connectionBox.AddMany([(self.title1,0,wx.EXPAND),
                                    (self.connectionLabel, 0, wx.EXPAND),
                                    (self.connectionInput, 1, wx.EXPAND),
                                    (self.connectBtn, 0, wx.EXPAND),
                                    (self.disconnectBtn, 0, wx.EXPAND)])

        # 电源开关
        self.powerBox = wx.BoxSizer(wx.HORIZONTAL)
        self.title2 = wx.StaticText(self, label='电源开关：')
        self.turnOnBtn = wx.Button(self, label='Turn On')
        self.turnOffBtn = wx.Button(self, label='Turn Off')
        self.powerBox.AddMany([(self.title2,0,wx.EXPAND),
                               (self.turnOnBtn, 0, wx.EXPAND),
                               (self.turnOffBtn, 0, wx.EXPAND)])

        # 电源 and 电压的设置
        self.voltageCurrentBox = wx.BoxSizer(wx.HORIZONTAL)
        self.title3 = wx.StaticText(self, label='电源电压大小设置：')
        self.channelLabel = wx.StaticText(self, label='Channel')
        self.channelInput = wx.TextCtrl(self)
        self.voltageLabel = wx.StaticText(self, label='Voltage (V)')
        self.voltageInput = wx.TextCtrl(self)
        self.currentLabel = wx.StaticText(self, label='Current (A)')
        self.currentInput = wx.TextCtrl(self)
        self.setVoltageCurrentBtn = wx.Button(self, label='Set Voltage/Current')
        self.voltageCurrentBox.AddMany([(self.title3,0,wx.EXPAND),
                                        (self.channelLabel, 0, wx.EXPAND),
                                        (self.channelInput, 1, wx.EXPAND),
                                        (self.voltageLabel, 0, wx.EXPAND),
                                        (self.voltageInput, 1, wx.EXPAND),
                                        (self.currentLabel, 0, wx.EXPAND),
                                        (self.currentInput, 1, wx.EXPAND),
                                        (self.setVoltageCurrentBtn, 0, wx.EXPAND)])

        # 事件处理部分
        self.connectBtn.Bind(wx.EVT_BUTTON, self.connect)
        self.disconnectBtn.Bind(wx.EVT_BUTTON, self.disconnect)
        self.turnOnBtn.Bind(wx.EVT_BUTTON, self.turn_on)
        self.turnOffBtn.Bind(wx.EVT_BUTTON, self.turn_off)
        self.setVoltageCurrentBtn.Bind(wx.EVT_BUTTON, self.set_voltage_current)

        # 将各部分布局管理器添加在主布局管理器
        vbox.AddMany([(self.connectionBox, 0, wx.EXPAND),
                      (self.powerBox, 0, wx.EXPAND),
                      (self.voltageCurrentBox, 0, wx.EXPAND)])

        self.SetSizer(vbox)

    def connect(self, event):
        address = self.connectionInput.GetValue()
        self.DP932A_controller = DP932A_Controller(address)
        print(f"Connected to DP932A at address {address}")

    def disconnect(self, event):
        # Implement disconnection logic here
        # Example: self.dp932a_controller.disconnect()
        print("Disconnected from DP932A")

    def turn_on(self, event):
        self.DP932A_controller.turn_on(1)

    def turn_off(self, event):
        self.DP932A_controller.turn_dowm(0)

    def set_voltage_current(self, event):
        channel = self.channelInput.GetValue()
        voltage = self.voltageInput.GetValue()
        current = self.currentInput.GetValue()
        self.DP932A_controller.set_V_and_I(channel, voltage, current)

if __name__ =="__main__":
    app =wx.App()
    frame = wx.Frame(None, title="DP932A Controller App", size=(1000, 500))
    DP932A_controller =DP932A_InstrParameters(frame,"DP932A_controller")
    frame.Show(True)
    app.MainLoop()