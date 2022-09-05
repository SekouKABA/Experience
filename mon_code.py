from matplotlib import pyplot as plt
import numpy as np, seaborn as sns 


sns.set_theme()
fig, ax = plt.subplots()
x = np.linspace(-10,10,100)

f = lambda x: np.sin(x)
ax.plot(x,f(x))

plt.show()


def test():
    return "Bienvenue"
