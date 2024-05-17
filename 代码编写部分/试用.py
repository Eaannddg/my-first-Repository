import wx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.animation import FuncAnimation


# 几种不同类型的波形生成函数
def generate_sine_wave(freq, duration, sample_rate):
    t = np.arange(0, duration, 1 / sample_rate)
    wave = np.sin(2 * np.pi * freq * t)
    return t, wave


def generate_square_wave(freq, duration, sample_rate):
    t = np.arange(0, duration, 1 / sample_rate)
    wave = np.sign(np.sin(2 * np.pi * freq * t))
    return t, wave


def generate_triangle_wave(freq, duration, sample_rate):
    t = np.arange(0, duration, 1 / sample_rate)
    wave = np.abs(2 * (t * freq - np.floor(t * freq + 0.5)))
    wave = 2 * wave - 1
    return t, wave


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Matplotlib in wxPython")
        self.panel = wx.Panel(self)

        # 设置参数
        self.frequency = 5  # 波形频率，单位Hz
        self.duration = 1  # 波形持续时间，单位秒
        self.sample_rate = 1000  # 采样率，单位Hz

        # 创建 Matplotlib 图形
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        self.ax.set_title('Waveform')
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Amplitude')
        self.ax.set_xlim(0, self.duration)
        self.ax.set_ylim(-1.1, 1.1)
        self.ax.grid(True)

        # 创建 Matplotlib 画布
        self.canvas = FigureCanvas(self.panel, -1, self.fig)

        # 创建下拉菜单
        waveform_choices = ['Sine', 'Square', 'Triangle']
        self.waveform_choice = wx.Choice(self.panel, choices=waveform_choices)
        self.waveform_choice.SetSelection(0)
        self.waveform_choice.Bind(wx.EVT_CHOICE, self.on_waveform_change)

        # 添加控件到界面
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.waveform_choice, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.panel.SetSizer(sizer)

        # 创建动画
        self.ani = FuncAnimation(self.fig, self.update, frames=range(int(self.sample_rate * self.duration)),
                                 blit=True, interval=10)

    # 下拉菜单事件处理函数
    def on_waveform_change(self, event):
        selection = self.waveform_choice.GetSelection()
        if selection == 0:
            self.generate_waveform = generate_sine_wave
        elif selection == 1:
            self.generate_waveform = generate_square_wave
        elif selection == 2:
            self.generate_waveform = generate_triangle_wave

    # 更新函数
    def update(self, frame):
        t, wave = self.generate_waveform(self.frequency, self.duration, self.sample_rate)
        self.line.set_data(t[:frame], wave[:frame])
        return self.line,


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
