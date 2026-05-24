# coding:utf-8
# @Author:xb
# @Time: 2024/3/13 8:06
# @File:matplotlib_直方图.py

# import matplotlib.pyplot as plt
# import numpy as np
# #随机数的种子，0-16
# np.random.seed(0)
# mu,sing = 100,20
# #其中100表示均值，20表示方差，size表示输出的size
# a = np.random.normal(mu,sing,size=100)
# #a表示统计的数据集，density指定柱子高度，histyype：直方图类型，facecolor：直方图颜色，alpha：透明度
# plt.hist(a,20,normed = 1,histtype='stepfilled',facecolor ='r',alpha = 0.75)
# plt.title('histogram')
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
mu, sig = 100, 20
a = np.random.normal(mu, sig, size=100)

plt.hist(a, 20, normed=1, histtype='stepfilled', facecolor='r', alpha=0.75)
plt.title('histogram')
plt.show()

