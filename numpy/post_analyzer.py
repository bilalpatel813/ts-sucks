import numpy as np

likes = np.array([120, 850, 430, 1200, 300, 950, 75])

print("Highest likes: ",np.max(likes))
print("Lowest likes: ",np.min(likes))
print("Average likes: ",np.mean(likes))
print("sorted likes: ",np.sort(likes))
print("Highest performing post: ",likes[likes>=500])
print("Performance Label: ",np.where(likes>=500,"High","Low"))
print("position of high performing post : ",np.where(likes>=500)[0])




