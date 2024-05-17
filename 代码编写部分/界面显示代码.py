import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 初始化图形
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
line, = ax.plot(x, np.sin(x))

# 更新函数，每次更新波形
def update(frame):
    line.set_ydata(np.sin(x + frame * 0.1))  # 更新波形数据
    return line,

# 创建动画
ani = FuncAnimation(fig, update, frames=range(100), interval=50)
plt.show()
