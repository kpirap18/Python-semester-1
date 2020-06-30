import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,4,7,9,13,46])
l = ['aaa','bbb','ccc','ddd','eee','fff']
e = [0,0,0,0.2,0,0]
#plt.figure(figsize=(10,10))
plt.pie(x,labels=l,explode=e)
plt.show()
