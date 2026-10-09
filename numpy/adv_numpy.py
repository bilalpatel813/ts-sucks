import numpy as np

# - Indexing :
a = np.array([10, 20, 30, 40, 50])

print(a[2]) # Normal indexing
print(a[[0,2,4]]) # adv indexing 

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(matrix[[0,2]])

# - Sorting :

S = np.array([40,60,20,30,10,70])
print("Unsorted Array: ",S)
print("Sorted Array: ",np.sort(S))
print("Sorted array reverse: ",np.sort(S)[::-1])
print("indices of element before sorting: ",np.argsort(S))

S2d = np.array([[10,40,30],
                [20,100,80]])
print("Coloumn:",np.sort(S2d,axis=0))
print("Row:",np.sort(S2d,axis=1))

# - Unique : repested values are removed and the result are sorted 

num = np.array([1,1,2,3,3,4,4,4,5,7,6,6])
unique_values,counts = np.unique(
    num,
    return_counts =True
)
print("Uniques Values: ",unique_values)
print("count: ",counts)

# - Missing & invalid values :

data  = np.array([1,np.nan,2,3,4,5,5])
print("Data: ",data)
print("Average of data: ",np.mean(data))

print("find Data : ",np.isnan(data))
print("count missing values: ",np.isnan(data).sum())
print("Cleaning Data: ",np.nan_to_num(data,nan=100))

#performance counter: loops vs vectorization
import time
numbers = list(range(1_000_000))

results = []

for number in numbers:
    results.append(number * 1.1)


users  = np.arange(1_000_000)
start = time.perf_counter()
result =  users * 1.1
end = time.perf_counter() - start
print("time taken :",end)
