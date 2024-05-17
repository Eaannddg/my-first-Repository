import wx
from DP932A_INSTR import DP932A_Controller
class DP932A_ControllerPanel(wx.Panel):

    def __init__(self, parent, DP932A_controller, **kwargs):
        super(DP932A_ControllerPanel, self).__init__(parent)
        self.DP932A_controller = DP932A_controller
        self.InitUI()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)



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


        # 查询电源和电压
        self.queryVoltageCurrentBox = wx.BoxSizer(wx.HORIZONTAL)
        self.title5 = wx.StaticText(self, label='查询电源电压和电流：')
        self.queryChannelLabel = wx.StaticText(self, label='Channel')
        self.queryChannelInput = wx.TextCtrl(self)
        self.queryBtn = wx.Button(self, label='查询电压和电流')
        self.queryVoltageCurrentBox.AddMany([(self.title5, 0, wx.EXPAND),
                                             (self.queryChannelLabel, 0, wx.EXPAND),
                                             (self.queryChannelInput, 0, wx.EXPAND),
                                             (self.queryBtn, 0, wx.EXPAND)])

        # 设置波形
        self.waveformBox = wx.BoxSizer(wx.HORIZONTAL)
        self.title4 = wx.StaticText(self, label='设置波形：')
        self.cycleLabel = wx.StaticText(self, label="Cycle")
        self.cycleInput = wx.TextCtrl(self)
        self.valueLabel = wx.StaticText(self, label="Value")
        self.valueInput = wx.TextCtrl(self)
        self.setwaveformBtn = wx.Button(self, label="Set Cycle/Value")
        self.waveformBox.AddMany([(self.title4, 0, wx.EXPAND),
                                  (self.cycleLabel, 0,wx.EXPAND),
                                  (self.cycleInput, 1, wx.EXPAND),
                                  (self.valueLabel,0,wx.EXPAND),
                                  (self.valueInput, 1, wx.EXPAND),
                                  (self.setwaveformBtn,0,wx.EXPAND)])

        # 清除事件寄存器
        self.clearEventsBox = wx.BoxSizer(wx.HORIZONTAL)
        self.title6 = wx.StaticText(self, label='清除事件寄存器：')
        self.clearEventsBtn = wx.Button(self, label='清除事件寄存器')
        self.clearEventsBox.AddMany([(self.title6, 0, wx.EXPAND),
                                     (self.clearEventsBtn, 0, wx.EXPAND)])




        #  事件处理部分
        self.turnOnBtn.Bind(wx.EVT_BUTTON, self.turn_on)
        self.turnOffBtn.Bind(wx.EVT_BUTTON, self.turn_off)
        self.setVoltageCurrentBtn.Bind(wx.EVT_BUTTON, self.set_voltage_current)
        self.setwaveformBtn.Bind(wx.EVT_BUTTON, self.set_cycle)
        self.queryBtn.Bind(wx.EVT_BUTTON, self.query_voltage_current)
        self.clearEventsBtn.Bind(wx.EVT_BUTTON, self.clear_events)

        # 将各部分布局管理器添加在主布局管理器
        vbox.AddMany( [(self.powerBox, 0, wx.EXPAND),
                      (self.voltageCurrentBox, 0, wx.EXPAND),
                      (self.queryVoltageCurrentBox, 0, wx.EXPAND),
                      (self.waveformBox,0,wx.EXPAND),
                      (self.clearEventsBox,0,wx.EXPAND)])


        self.SetSizer(vbox)


    def turn_on(self, event):
        self.DP932A_controller.turn_on(1)

    def turn_off(self, event):
        self.DP932A_controller.turn_dowm(0)

    def set_voltage_current(self, event):
        channel = self.channelInput.GetValue()
        voltage = self.voltageInput.GetValue()
        current = self.currentInput.GetValue()
        self.DP932A_controller.set_V_and_I(channel, voltage, current)

    def query_voltage_current(self, event):
        channel = self.queryChannelInput.GetValue()
        try:
            if channel:
                command = f":APPLy? {channel}"
            else:
                command = ":APPLy?"

            response = self.DP932A_controller.query_V_and_I(channel)
            print(f"查询结果: {response}")
        except Exception as e:
            print("查询电源设置异常")

    def set_cycle(self,event):
        cycle =self.cycleInput.GetValue()
        value =self.valueInput.GetValue()
        self.DP932A_controller.set_cycle(cycle,value)

    def clear_events(self, event):
        try:
            command = "*CLS"
            self.DP932A_controller.clear_events()
            print("事件寄存器已清除")
        except Exception as e:
            print("清除事件寄存器异常")



# "TCPIP0::192.168.1.65::inst0::INSTR"


if __name__ =="__main__":
    app =wx.App()
    frame = wx.Frame(None, title="DP932A Controller App", size=(1000, 500))
    DP932A_controller =DP932A_ControllerPanel(frame,"DP932A_controller")
    frame.Show(True)
    app.MainLoop()
