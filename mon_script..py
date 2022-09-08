from cProfile import label
import numpy as np, seaborn as sns, random 
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

liste_1 = [1,2,8,45]
liste_2 = [i**2 for i in random.sample(range(1,20),4)]

a = zip(liste_1,liste_2)


b = np.array([1,4,5])
c = np.array([1,2,3])

print(b[c])





