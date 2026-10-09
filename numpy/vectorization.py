import numpy as np
sales = np.array([100,500,600,1000])
tax = sales * 0.18
total_sales = sales - tax
print("sales: ",sales)
print("tax: ",tax)
print("totalsales : ",total_sales)
likes = np.array([1000,500,100,250,2000])
labels = np.where(likes<500,"Low","High")
print(labels)
#Vectorization : can append any opreation on np array with out needing loops 
#- vectorization conditional logic: np.where(condition, value_if_true, value_if_false)
