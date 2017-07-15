import numpy as np
import matplotlib. pyplot as plt
x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])

x1=np.mean(x)
y1=np.mean(y)

slope=(np.sum((x-x1)*(y-y1)))/(np.sum(np.power((x-x1),2)))

coeff=y1-(slope*x1)

arr = [slope*i + coeff for i in x]

plt.scatter(x,y)
plt.plot(x,arr)
plt.show()
