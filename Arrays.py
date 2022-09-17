import numpy as np

#Zero Dimensional Array
arr1=np.array(42)
print(arr1)
print(arr1.shape)
print(arr1.ndim)


#One Dimensional Array

arr=np.array([1,2,3,4,5])
print(arr)
print(arr.shape)
print(arr.ndim)

print(type(arr))


#Two Dimensional Array

arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr2.shape)
print(arr2.ndim)

#Three Dimensional Array

arr3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3)
print(arr3.shape)
print(arr3.ndim)

#N dimensional array

arr4 = np.array([1,2,3,4], ndmin=5)

print(arr4)
print("No. of dimensions: ",arr4.ndim)
print(arr4.shape)


