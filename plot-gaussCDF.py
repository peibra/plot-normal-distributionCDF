from matplotlib import pyplot as plt
import numpy as np

from gaussCDF import normal_distributionCDF

x = np.arange(-3, 3, 0.01)

y = normal_distributionCDF(x, 30)
plt.plot(x, y)

plt.grid()
plt.show()
