#Gerador e gráffico 3d rtirado do instagram @python.hub
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as  np

x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
y = x.copy().T
z = np.cos(x**2  + y**3)
fig = plt.figure()

ax = plt.axes(projection = '3d')

ax.plot_surface(x, y, z, cmap ='viridis' ,edgecolor = 'green')
ax.set_title('Surface plot python.hub')
plt.show()