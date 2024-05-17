# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc



###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel1(wx.Panel):

    def __init__(self, parent,DP932A_controller,id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(765, 232), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        CH1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"CH1"), wx.HORIZONTAL)

        self.CH = "CH1"
        self.DP932A_controller =DP932A_controller

        DisplayScreen = wx.BoxSizer(wx.VERTICAL)

        DisplayScreen.Add((0, 10), 1, wx.EXPAND, 5)

        CurrentBox = wx.BoxSizer(wx.VERTICAL)

        self.volatge = wx.StaticText(CH1.GetStaticBox(), wx.ID_ANY, u"电流：0 A", wx.Point(-1, -1), wx.DefaultSize, 0)
        self.volatge.Wrap(-1)

        self.volatge.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))

        CurrentBox.Add(self.volatge, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        DisplayScreen.Add(CurrentBox, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        DisplayScreen.Add((0, 10), 1, wx.EXPAND, 5)

        VolatgeBOX = wx.BoxSizer(wx.VERTICAL)

        self.current = wx.StaticText(CH1.GetStaticBox(), wx.ID_ANY, u"电压：0 V", wx.Point(-1, -1), wx.DefaultSize, 0)
        self.current.Wrap(-1)

        self.current.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        VolatgeBOX.Add(self.current, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        DisplayScreen.Add(VolatgeBOX, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        DisplayScreen.Add((0, 10), 1, wx.EXPAND, 5)

        PowerBox = wx.BoxSizer(wx.VERTICAL)

        self.power = wx.StaticText(CH1.GetStaticBox(), wx.ID_ANY, u"功率：0 W", wx.DefaultPosition, wx.DefaultSize, 0)
        self.power.Wrap(-1)

        self.power.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        PowerBox.Add(self.power, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        DisplayScreen.Add(PowerBox, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        DisplayScreen.Add((0, 10), 1, wx.EXPAND, 5)

        CH1.Add(DisplayScreen, 1, wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(CH1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_VERTICAL)
        self.m_staticline1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        CH1.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        settings_interface = wx.BoxSizer(wx.VERTICAL)

        current_voltage_setting = wx.BoxSizer(wx.HORIZONTAL)

        self.Set = wx.StaticText(CH1.GetStaticBox(), wx.ID_ANY, u"Set :  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Set.Wrap(-1)

        self.Set.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "华文中宋"))

        current_voltage_setting.Add(self.Set, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.voltageInput = wx.TextCtrl(CH1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_CENTER)
        current_voltage_setting.Add(self.voltageInput, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.unit_of_V = wx.StaticText(CH1.GetStaticBox(), wx.ID_ANY, u"V", wx.DefaultPosition, wx.DefaultSize, 0)
        self.unit_of_V.Wrap(-1)

        self.unit_of_V.SetFont(
            wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Cambria"))

        current_voltage_setting.Add(self.unit_of_V, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.currentInput = wx.TextCtrl(CH1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_CENTER)
        current_voltage_setting.Add(self.currentInput, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.unit_of_A = wx.StaticText(CH1.GetStaticBox(), wx.ID_ANY, u"A", wx.DefaultPosition, wx.DefaultSize, 0)
        self.unit_of_A.Wrap(-1)

        self.unit_of_A.SetFont(
            wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Cambria"))

        current_voltage_setting.Add(self.unit_of_A, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.set_button = wx.Button(CH1.GetStaticBox(), wx.ID_ANY, u"confirm", wx.DefaultPosition, wx.Size(80, -1), 0)
        self.set_button.SetFont(
            wx.Font(9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Book Antiqua"))

        current_voltage_setting.Add(self.set_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        settings_interface.Add(current_voltage_setting, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        OVPBox = wx.BoxSizer(wx.HORIZONTAL)

        self.ovp = wx.StaticText(CH1.GetStaticBox(), wx.ID_ANY, u"OVP : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ovp.Wrap(-1)

        self.ovp.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "华文中宋"))

        OVPBox.Add(self.ovp, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ovp_value = wx.TextCtrl(CH1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(150, -1), wx.TE_CENTER)
        OVPBox.Add(self.ovp_value, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.unit_of_V1 = wx.StaticText(CH1.GetStaticBox(), wx.ID_ANY, u"V", wx.DefaultPosition, wx.DefaultSize, 0)
        self.unit_of_V1.Wrap(-1)

        self.unit_of_V1.SetFont(
            wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Cambria"))

        OVPBox.Add(self.unit_of_V1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        OVPBox.Add((20, 0), 0, wx.EXPAND, 5)

        self.ovp_set = wx.Button(CH1.GetStaticBox(), wx.ID_ANY, u"confirm", wx.DefaultPosition, wx.DefaultSize, 0)
        OVPBox.Add(self.ovp_set, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        settings_interface.Add(OVPBox, 1, wx.EXPAND, 5)

        OCPBox = wx.BoxSizer(wx.HORIZONTAL)

        self.ocp = wx.StaticText(CH1.GetStaticBox(), wx.ID_ANY, u"OCP : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ocp.Wrap(-1)

        self.ocp.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "华文中宋"))

        OCPBox.Add(self.ocp, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ocp_value = wx.TextCtrl(CH1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(150, -1), wx.TE_CENTER)
        OCPBox.Add(self.ocp_value, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.unit_of_A1 = wx.StaticText(CH1.GetStaticBox(), wx.ID_ANY, u"A", wx.DefaultPosition, wx.DefaultSize, 0)
        self.unit_of_A1.Wrap(-1)

        self.unit_of_A1.SetFont(
            wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Cambria"))

        OCPBox.Add(self.unit_of_A1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        OCPBox.Add((20, 0), 0, wx.EXPAND, 5)

        self.ocp_set = wx.Button(CH1.GetStaticBox(), wx.ID_ANY, u"confirm", wx.DefaultPosition, wx.DefaultSize, 0)
        OCPBox.Add(self.ocp_set, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        settings_interface.Add(OCPBox, 1, wx.EXPAND, 5)

        CH1.Add(settings_interface, 2, wx.EXPAND, 5)

        self.m_staticline11 = wx.StaticLine(CH1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_VERTICAL)
        self.m_staticline11.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        CH1.Add(self.m_staticline11, 0, wx.EXPAND | wx.ALL, 5)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText14 = wx.StaticText(CH1.GetStaticBox(), wx.ID_ANY, u"电源：", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText14.Wrap(-1)

        bSizer9.Add(self.m_staticText14, 0, wx.ALL, 5)

        self.power_switch = wx.ToggleButton(CH1.GetStaticBox(), wx.ID_ANY, u"on/off", wx.DefaultPosition,
                                            wx.Size(90, 40), 0)
        self.power_switch.SetFont(
            wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))

        bSizer9.Add(self.power_switch, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer9.Add((0, 5), 1, wx.EXPAND, 5)

        self.m_staticText141 = wx.StaticText(CH1.GetStaticBox(), wx.ID_ANY, u"ovp/ocp:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText141.Wrap(-1)

        bSizer9.Add(self.m_staticText141, 0, wx.ALL, 5)

        self.ovp_switch = wx.ToggleButton(CH1.GetStaticBox(), wx.ID_ANY, u"OVP", wx.DefaultPosition, wx.Size(80, -1), 0)
        bSizer9.Add(self.ovp_switch, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ocp_switch = wx.ToggleButton(CH1.GetStaticBox(), wx.ID_ANY, u"OCP", wx.DefaultPosition, wx.Size(80, -1), 0)
        bSizer9.Add(self.ocp_switch, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer9.Add((0, 5), 1, wx.EXPAND, 5)

        CH1.Add(bSizer9, 1, wx.EXPAND, 5)

        self.SetSizer(CH1)
        self.Layout()
        self.update_values_timer = wx.Timer()
        self.update_values_timer.SetOwner(self, self.update_values_timer.GetId())

        # Connect Events
        self.set_button.Bind(wx.EVT_BUTTON, self.set_v_and_I)
        self.ovp_value.Bind(wx.EVT_TEXT, self.set_overvoltage_protection_value)
        self.ocp_set.Bind(wx.EVT_BUTTON, self.set_overcurrent_protection_state)
        self.power_switch.Bind(wx.EVT_TOGGLEBUTTON, self.on_and_off)
        self.ovp_switch.Bind(wx.EVT_TOGGLEBUTTON, self.ovp_on_and_off)
        self.ocp_switch.Bind(wx.EVT_TOGGLEBUTTON, self.ocp_on_and_off)
        self.Bind(wx.EVT_TIMER, self.update_values, id=self.update_values_timer.GetId())

    def __del__(self):
        pass


# Virtual event handlers, override them in your derived class


    def set_v_and_I(self, event):
        voltage = self.voltageInput.GetValue()
        current = self.currentInput.GetValue()
        self.DP932A_controller.set_V_and_I(self.CH, voltage, current)
        event.Skip()


    def set_overvoltage_protection_value(self, event):
        value = self.ovp_value.GetValue()
        self.DP932A_controller.set_overvoltage_protection_value(self.CH, value)
        event.Skip()


    def set_overcurrent_protection_value(self, event):
        value = self.ocp_value.GetValue()
        self.DP932A_controller.set_overcurrent_protection_value(self.CH, value)
        event.Skip()


    def on_and_off(self, event):
        if self.power_switch.GetValue():
            self.DP932A_controller.turn_on(self.CH)
        else:
            self.DP932A_controller.turn_dowm(self.CH)
        event.Skip()


    def ovp_on_and_off(self, event):
        if self.ovp_switch.GetValue():
            self.DP932A_controller.enable_overvoltage_protection(self.CH)
        else:
            self.DP932A_controller.disable_overvoltage_protection(self.CH)
        event.Skip()


    def ocp_on_and_off(self, event):
        if self.ocp_value.GetValue():
            self.DP932A_controller.enable_overcurrent_protection(self.CH)
        else:
            self.DP932A_controller.disable_overcurrent_protection(self.CH)
        event.Skip()


    def update_values(self, event):
        voltage_value = self.voltageInput.GetValue()
        current_value = self.currentInput.GetValue()
        power_value = voltage_value * current_value

        # 更新文本控件的值
        self.volatge.SetLabel(u"电流：{} A".format(current_value))
        self.current.SetLabel(u"电压：{} V".format(voltage_value))
        self.power.SetLabel(u"功率：{} W".format(power_value))

        event.Skip()

