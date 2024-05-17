import pyvisa
class DP932A_Controller:
    name = "DP932A_Controller"
    isMotor = False
    isPower = True
    isLaser = False
    def __init__(self,address):
        rm =pyvisa.ResourceManager()
        try:
            self.open =rm.open_resource(address)
            print("地址连接正常")
        except Exception as e:
            print("地址连接异常")

    def disconnect(self):
        try:
            self.close()
            print("仪器断开连接")
        except Exception as e:
            print("断开连接失败")


    def turn_on(self,state):
        try:
            self.open.write(f":OUTPut {state}")
            print("打开电源")
        except Exception as e:
            print("电源打开异常")

    def turn_dowm(self,state):
        try:
            self.open.write(f":OUTPut {state}")
            print("关闭电源")
        except Exception as e:
            print("关闭电源异常")


    def set_V_and_I(self,channel,voltage,current):
        try:
            command =f":APPLy {channel},{voltage},{current}"
            self.open.write(command)
            print(f"设置通道 {channel} 电压为 {voltage} V，电流为 {current} A")
        except Exception as e:
            print("设置电源异常")

    def set_overvoltage_protection_value(self, source, value):
        try:
            if 0 <= value <= 35.2:
                command = f":OUTPut:OVP:VALue {source},{value}"
                self.open.write(command)
                print(f"成功设置 {source} 通道的过压保护值为: {value} V")
            else:
                print("提供的过压保护值超出范围，请提供介于 0 到 35.2 之间的值")
        except Exception as e:
            print("设置过压保护值异常:", e)

    def set_overcurrent_protection_value(self, source, value):
        try:
            if 0 <= value <= 3.3:
                command = f":OUTPut:OCP:VALue {source},{value}"
                self.open.write(command)
                print(f"成功设置 {source} 通道的过流保护值为: {value} A")
            else:
                print("提供的过流保护值超出范围，请提供介于 0 到 3.3 之间的值")
        except Exception as e:
            print("设置过流保护值异常:", e)

    def enable_overvoltage_protection(self, source):
        try:
            command = f":OUTPut:OVP:STATe {source},1"  # 打开指定通道的过压保护功能
            self.open.write(command)
            print(f"成功打开 {source} 通道的过压保护功能")
        except Exception as e:
            print("打开过压保护功能异常:", e)

    def disable_overvoltage_protection(self, source):
        try:
            command = f":OUTPut:OVP:STATe {source},0"  # 关闭指定通道的过压保护功能
            self.open.write(command)
            print(f"成功关闭 {source} 通道的过压保护功能")
        except Exception as e:
            print("关闭过压保护功能异常:", e)

    def enable_overcurrent_protection(self, source):
        try:
            command = f":OUTPut:OCP:STATe {source},1"
            self.open.write(command)
            print(f"成功打开 {source} 通道的过流保护功能")
        except Exception as e:
            print("设置过流保护状态异常:", e)

    def disable_overcurrent_protection(self, source):
        try:
            command = f":OUTPut:OCP:STATe {source},0"
            self.open.write(command)
            print(f"成功关闭 {source} 通道的过流保护功能")
        except Exception as e:
            print("设置过流保护状态异常:", e)

