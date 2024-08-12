import numpy as np

# array1=np.array([1,2,3])# Vector
# # print(type(array1))
# # print(array1.ndim)
# # print(array1.shape)
# array2=np.array([[1,2,3],[4,5,6]])
# # print(type(array2))
# # print(array2.ndim)
# # print(array2.shape)
# # print('This a single dimentional array',array1)
# # print ('Two dimentional array', array2)

# #indexing in numpy
# #positive indexing
# # print('print the first vector/list',array2[0])
# # print('print the second vector/list',array2[1])

# array3=np.array([[3,4,5,6],[6,7,8,9]])
# # array3.reshape(2,4)
# # print(array3)
# # print('the last vector using negative index',array3[-1])
# # print('the second element in second vector is', array3[1,1])

# # print('using slicing print the first element of the array', array3[:,0])
# # print('using slicing print the second element of the second and third vector', array3[1:,1])
# # print(array3[1:,1:])

# # reassign value
# # array3[-1,-1]=10
# # print(array3)


# # array4=np.array([1,2,3,4,5,6,7,8])
# # arr=array4.reshape(4,2)
# # print(arr)

# # array_=np.array([[[1,2,3],[3,6,7]],[[3,4,5],[6,9,0]]])
# # print(array_.ndim)
# # print(array_.shape)
# # b=array_.reshape(1,-1)
# # print(b)
# # print(b.ndim)
# # print(b.shape)
# # a=np.reshape(array_,(2,-1))
# # print(a)
# # print(a.ndim)
# # print(a.shape)

# # a = np.array([[1,2,3], [4,5,6]])
# # a.reshape(3,-1)
# # print(a)

# array_a = np.array([[1,2,3],[4,5,6]])
# array_b=np.array([[5,6,7],[8,9,10]])
# # array_a[0]=9
# # print(array_a)
# # array_a[:,0]=9
# # print('second result',array_a)
# list_=[6,7,8]
# # array_a[0]=list_
# # print(array_a)
# #using element wise in an array
# # print(array_a*2)
# # print(array_a+2)
# # print(array_a-array_b)
# # print(array_a*array_b[0,1])
# # print(list_+[2])


# #Data type that supported by numpy
# array_f = np.array([[1,2,3],[4,5,6]], dtype = np.float32)
# # print(array_f)
# # array_c=np.array([[1,2,3],[8,9,0]], dtype=np.complex128)
# # print(array_c)
# # array_s=np.array([[1,2,3],[8,9,0]], dtype=np.int32)
# # print(array_s)


# # Arrays of Zeros and 1
# # empty_a=np.empty(shape=(2,3))
# # print(empty_a)

# # zero_a= np.zeros(shape=(2,3), dtype=np.int16)
# # print(zero_a)


matrix_a=np.array([[1,0,9,2,2],[3,23,4,5,1],[0,2,3,4,1]])
# arr=np.empty_like(matrix_a)
# # print(arr)

zero_=np.zeros_like(matrix_a)
print(zero_)


# arrange_=np.arange(30)
# # print(arrange_)
# arrange1=np.arange(start=10,stop=30,step=5)
# print(arrange1)