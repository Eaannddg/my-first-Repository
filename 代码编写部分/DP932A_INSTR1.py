import pyvisa
class DP932A_Controller:
    def __init__(self,address):
        rm =pyvisa.ResourceManager()
        try:
            self.open =rm.open_resource(address)
            print("地址连接正常")
        except Exception as e:
            print("地址连接异常")



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

    def set_cycle(self,cycle,value):
        try:
            command =f":TIMEr:CYCLES {cycle},{value}"
            self.write(command)
        except Exception as e:
            print("设置波形器循环异常")

    def set_query(self):
        try:
            self.write(":TIME:CYCLE? ")
        except Exception as e:
            print("查询波形状况异常")