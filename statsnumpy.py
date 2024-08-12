import numpy as np

array1=np.array([[1,2,3],[4,5,0]])
print(np.mean(array1))
print('Return minimum value in the array',np.min(array1))
print('Return minimum value axis wise (downward)',np.amin(array1,axis=0))
print('Return minimum value in horizontal',np.amin(array1,axis=1))
print('Return the median of the matrix',np.median(array1))
print('Return the average',np.average(array1))
print('return the variance of the array',np.var(array1))
print('return the std of the array',np.std(array1))
covariance=np.cov(array1)
print('print covariance',covariance)
