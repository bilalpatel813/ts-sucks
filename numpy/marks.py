import numpy as np
marks = np.array([70,60,80,85,90,93])
total_marks = np.sum(marks)
avg_marks = np.mean(marks)
highest_marks = np.max(marks)
lowest_marks = np.min(marks)
print("marks obtainted: ",marks)
print("Total Marks: ",total_marks)
print("average marks: ",avg_marks)
print("Highest marks: ",highest_marks)
print("lowest marks: ",lowest_marks)
print("marks above 75: ",marks[marks>75])
print("standerd deviation: ",np.std(marks))
print("number of subjects scored above 75 marks: ",np.size(marks[marks>75]))
print("sorted marks: ",marks.reshape(6,1))


students = np.array([
    [78, 82, 91],
    [65, 70, 68],
    [92, 88, 95],
    [55, 60, 58]
])

print("shape of student array: ",np.shape(students))
print("total marks of students:",np.sum(students))
print("average of everything: ",np.mean(students)//2)
print("avg of each student: ",np.mean(students,axis=1)//2)
print("average of each subject",np.mean(students,axis=0)//2)
print("Highest marks of students: ",np.max(students,axis=1))
print("Lowest marks of students: ",np.min(students,axis=1))