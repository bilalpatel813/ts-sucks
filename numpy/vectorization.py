import numpy as np
sales = np.array([100,500,600,1000])
tax = sales * 0.18
total_sales = sales - tax
print("sales: ",sales)
print("tax: ",tax)
print("totalsales : ",total_sales)

#Vectorization : can append any opreation on np array with out needing loops 
