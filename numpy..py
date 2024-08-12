import numpy as np

array1=np.array([1,2,3])# Vector
# print(type(array1))
# print(array1.ndim)
# print(array1.shape)
array2=np.array([[1,2,3],[4,5,6]])
# print(type(array2))
# print(array2.ndim)
# print(array2.shape)
# print('This a single dimentional array',array1)
# print ('Two dimentional array', array2)

#indexing in numpy
#positive indexing
# print('print the first vector/list',array2[0])
# print('print the second vector/list',array2[1])

array3=np.array([[3,4,5],[6,7,8],[5,9,0]])
# print('the last vector using negative index',array3[-1])
# print('the second element in second vector is', array3[1,1])

# print('using slicing print the first element of the array', array3[:,0])
# print('using slicing print the second element of the second and third vector', array3[1:,1])
# print(array3[1:,1:])

# reassign value
# array3[-1,-1]=10
# print(array3)


array4=np.array([1,2,3,4,5,6,7,8])
# arr=array4.reshape(4,2)
# print(arr)

array_=np.array([[[1,2,3],[3,6,7]],[[3,4,5],[6,9,0]]])
print(array_.ndim)
print(array_.shape)
print(array_)