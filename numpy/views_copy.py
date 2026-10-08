import numpy as np

#views : changes applied on same array
a = np.array([10,20,30,40])

b= a[1:3] # made another array by silicing of previous array
print("before view a :" ,a,"\nb array: ",b)
b[0] = 999
print("after view a : ",a)

#copy: changes applied on copy array 

m = np.array([10,20,30,40])

n = m[:4].copy() # made copy of previous element with copy()
print("m :",m,"\nn array:",n)
n[0] = 9999
print("after copy m array: ",m,"\nn array: ",n)

