import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,5000000)
y = np.exp(-x*x)
plt.semilogy(x,y)
plt.show()
