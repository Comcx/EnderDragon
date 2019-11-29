# 导入包
import pandas as pd

from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用于画图时显示中文

url = "iris.data"
names = ['花萼-length', '花萼-width', '花瓣-length', '花瓣-width', 'class']
dataset = pd.read_csv(url, names=names)

# ************************可视化显示*************************************#
# 显示直方图
dataset.hist()  # 数据直方图histograms


# 显示散点图
dataset.plot(x='花萼-length', y='花萼-width', kind='scatter')  # 散点图，x轴表示花萼长度，y轴表示花萼宽度

# 显示箱图
# kind='box'绘制箱图,包含子图且子图的行列布局layout为2*2，子图共用x轴、y轴刻度，标签为False
dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)

# kde图
# KDE图，也被称作密度图(Kernel Density Estimate,核密度估计)
dataset.plot(kind='kde')
plt.show()
