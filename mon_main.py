from matplotlib import pyplot as plt
import numpy as np, seaborn as sns 
from mpl_toolkits.mplot3d import axes3d

sns.set_theme()
ax =plt.axes(projection ="3d")

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)

X,Y = np.meshgrid(x,y)


f = lambda x,y: np.sin(x) + np.cos(x+y)
ax.plot(x,f(X,Y))

plt.show()