from cProfile import label
import numpy as np, seaborn as sns, random 
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

sns.set_theme()

fig, ax = plt.subplots()
x = np.linspace(-10,10,1000)

f = lambda x: np.sin(x)
y = f(x)
xnew = (x[:-1]+x[1:])/2
ynew = (y[1:]-y[:-1])/(x[1:]-x[:-1])

ax.plot(x,y,c="red",label="f(x)")
ax.plot(xnew,ynew,label="f'(x)")
ax.legend()



plt.show()


