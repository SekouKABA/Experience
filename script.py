from cProfile import label
from json import load
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.animation as animation
import seaborn as sns 
from mpl_toolkits.mplot3d import Axes3D

# ax = plt.axes(projection="3d")

# f = lambda x,y: np.sin(x)+ np.cos(x+y)

# x = np.linspace(0,5,100)
# y = np.linspace(0,5,100)

# X,Y = np.meshgrid(x,y)

# Z =f(X,Y)
# ax.plot_surface(X,Y,Z,cmap="plasma")
# plt.show()

# x = np.linspace(0,5,100)
# y = np.linspace(0,5,100)
# X,Y = np.meshgrid(x,y)
# f = lambda x,y: np.sin(x)+np.cos(x+y)

# Z = f(X,Y)
# ax = plt.axes(projection="3d")

# ax.contourf(X,Y,Z)
# plt.show()

# age_men = [25,11,68,18,27,28,15,43,58,63,43,65,51,36,33,26,23,49,58]
# age_woman =[48,57,59,25,19,37,18,56,22,25,56,25,14,49,53,45,46,19,28,70]
# fig, ax = plt.subplots()

# ax.hist([age_men,age_woman],edgecolor="k",color=["#A0CF5E","#E76D3C"])
# plt.show()
f = lambda x: 1/(np.sqrt(2*np.pi))*np.exp(-1/2*x**2)

fig, ax = plt.subplots()
x = np.linspace(-10,10,1000)
ax.plot(x,f(x))
plt.show()




