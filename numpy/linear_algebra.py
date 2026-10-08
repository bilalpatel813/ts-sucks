import numpy as np
# linear algebra: 
# - elemet_wise multiplication(*):

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print("array a:",a)
print("array b:",b)
print("dot product of a & b: ",np.dot(a,b))

# - matrix  multiplication(@):
rng = np.random.default_rng(42)
m = rng.integers(0,10,size=(2,2))
n = rng.integers(0,10,size=(2,2))

print("array m:",m)
print("array n:",n)
print("Matrix multiplication of m & n: ",m @ n)

print("element-wise multiplication: ",m*n)


# - Solving equation:

#1 - 2x + y = 5
#2 - x + 3y = 2 -> 2x + 6y = 4 --3
A = np.array([
    [2, 1],
    [1, 3]
])
B = np.array([5,2])
print("linear algebaric solution[x,y] of equation  \n2x + y = 5\nx + 3y = 2\n",np.linalg.solve(A,B))

