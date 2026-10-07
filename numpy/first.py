import numpy as np

marks = np.array([10,20,30])

mark =  [10,20,30]

print("np array * 2:",marks *2)
print("List repetation in normal array")
print("array * 2:",mark *2)

print("dimension: ",marks.ndim)
print("type of np array:",marks.dtype)
print("size of np array: ",marks.size)
print("size of each of dimension of np elements: ",marks.shape)
print("------------")
print("two dimensional array ")
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70,80,90]
])

print(matrix)
print("dimension: ",matrix.ndim)
print("type of np array:",matrix.dtype)
print("size of np array: ",matrix.size)
print("size of each of dimension of np elements: ",matrix.shape)

print("Silicing")
print("silicing in 1d array: ",marks[1:4])
print("silicing in 2d array:\n ",matrix[0:1])

print(np.arange(1,10)) #short form to create array in np
print(np.zeros((2,3))) #all 0
print(np.full((3,3),7)) #all 7

n = np.arange(12)
print("n:",n)
num = n.reshape(2,6)
print("reshape 1d to 2d :",num)

#Basic statistics

print("sum of n elements: ",np.sum(n))
print("mean of n array:",np.mean(n))
print("max of n array:",np.max(n))
print("min of n array:",np.min(n))

# Boolean filtering 
a = np.arange(10)
print(a>=6)
print(a[a>=6])
