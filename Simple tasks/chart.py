import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,100)
y = np.sin(x)
plt.plot(x,y,':',label='sin(x)')
plt.title('$sin(x)$')
plt.axis([-5,5,-5,5])
plt.axis('equal')
plt.xticks(range(0,23,4))
plt.xlabel('x')
plt.ylabel('y $f(x)$')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
