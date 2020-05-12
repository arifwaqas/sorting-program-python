# %%
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

# %%
xs = np.array([10,100,1000,10000,20000,40000,60000,100000], dtype = np.float64)
ys = np.array([0.5,0.9,1.9,2.8,3.9,7.8,11.3,17.9], dtype = np.float64)
x1s = np.array([10,100,1000,10000,20000,40000,60000,100000], dtype = np.float64)
y1s = np.array([0.6,1.2,1.1,3.2,6.3,14.16,22.1,35.5], dtype = np.float64)
plt.xlabel('n')
plt.ylabel('time')
# plt.legend((line1, line2), ('MergeSort', 'BubbleSort'))
plt.scatter(xs,ys)
plt.plot(xs,ys,"-b",label="MergeSort")
plt.scatter(x1s,y1s)
plt.plot(x1s,y1s,"-r",label="BubbleSort")
plt.legend(loc="upper left")
# plt.ylim(-1.5, 2.0)
plt.show()

# %%
xs = np.array([10,100,1000,10000,20000,40000,60000,100000], dtype = np.float64)
ys = np.array([0.460,0.421,0.48,1.803,2.949,6.787,7.695,12.735], dtype = np.float64)
x1s = np.array([10,100,1000,10000,20000,40000,60000,100000], dtype = np.float64)
y1s = np.array([0.461,0.369,0.561,1.899,3.547,8.217,13.696,26.951], dtype = np.float64)
plt.xlabel('n')
plt.ylabel('time')

plt.scatter(xs,ys)
plt.plot(xs,ys,"-g",label="QuickSort")
plt.scatter(x1s,y1s)
plt.plot(x1s,y1s,"-r",label="SelectionSort")
plt.legend(loc="upper left")

plt.show()