import numpy as np

marks  = np.array([50,90,70,75,80])
bonus_marks = np.full(5,10)
total_marks = marks + bonus_marks
print("Marks Obtained: ",marks)
print("shape of marks array: ",np.shape(marks))
print("Bonus Marks: ",bonus_marks)
print("shape of bonus_marks array: ",np.shape(bonus_marks))
print("Total Marks: ",total_marks)

#BoardCasting : can merge elements of two different arrays of same index without loops
