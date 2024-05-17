import pyvisa

# 创建一个PyVISA的资源管理器
rm = pyvisa.ResourceManager()

# 打印可用的设备列表
print("可用设备列表：", rm.list_resources())

# 打开连接到设备
try:
    # 这里需要替换成你实际的设备地址，例如 GPIB0::9::INSTR，或者 USB0::0x1234::0x5678::INSTR
    instrument = rm.open_resource("TCPIP0::192.168.1.65::INSTR")

    # 查询设备信息
    print("设备信息:", instrument.query("*IDN?"))

    # 在这里可以进行更多的操作，例如发送命令并接收响应

    # 关闭连接
    instrument.close()
except pyvisa.errors.VisaIOError as e:
    print("连接设备时出现错误:", e)
