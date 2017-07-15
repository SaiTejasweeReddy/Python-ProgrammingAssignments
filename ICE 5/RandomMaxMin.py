import numpy as np

a = np.random.random((10,10))
print(a)
print ('Maximum value is ', np.max(a,axis=None))
print ('Minimum value is ', np.min(a,axis=None))