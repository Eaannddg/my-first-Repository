# 设置或查询指定通道的过流保护（OCP）值
# 参数:
#   - self: 类实例本身
#   - source: 通道名称，如 "CH1", "CH2", "CH3"
#   - value: 要设置的过流保护值（可选参数）
#   - lim: 可选参数，指定是查询最小值还是最大值
# 返回值:
#   若指定了value，则为设置后的过流保护值；若未指定value，则为查询得到的过流保护值
# 备注:
#   此函数用于设置或查询指定通道的过流保护值。如果未提供value参数，则表示进行查询操作。
def set_overcurrent_protection_value(self, source, value=None, lim=None):
    try:
        if value is not None:
            # 如果提供了value参数，则构建设置过流保护值的SCPI命令
            command = f":OUTPut:OCP:VALue {source},{value}"
            # 发送命令给仪器
            self.open.write(command)
            print(f"成功设置 {source} 通道的过流保护值为: {value} A")
            return value
        else:
            # 如果未提供value参数，则构建查询过流保护值的SCPI命令
            if lim is not None:
                command = f":OUTPut:OCP:VALue? {lim}"
            elif source is not None:
                command = f":OUTPut:OCP:VALue? {source}"
            else:
                command = ":OUTPut:OCP:VALue?"

            # 发送命令给仪器并获取返回值
            response = self.open.query(command)
            print(f"查询结果: {response}")
            return response
    except Exception as e:
        print("设置或查询过流保护值异常:", e)


# 设置过流保护值为最大值
ocp_max_value = set_overcurrent_protection_value(self, source="CH1", lim="MAXimum")

# 设置过流保护值为最小值
ocp_min_value = set_overcurrent_protection_value(self, source="CH2", lim="MINimum")

# 查询通道CH3的过流保护值
ocp_value_ch3 = set_overcurrent_protection_value(self, source="CH3")

# 设置通道CH1的过流保护值为3.5A
set_overcurrent_protection_value(self, source="CH1", value=3.5)

# 设置通道CH2的过流保护值为4.2A
set_overcurrent_protection_value(self, source="CH2", value=4.2)

