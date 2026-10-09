import numpy as np

rng0 = np.random.default_rng()

print("random element array(1-100): ",rng0.integers(1,100,size=5))

rng1 = np.random.default_rng(42)
print("Reproducible randomness: ",rng1.integers(1,100,5))

#exmaple:
rng = np.random.default_rng(42)

students = rng.integers(0,101,size=(10,3))
print("students: ",students)
print("average of each student: ",np.mean(students,axis=1))
print("average of each subjects: ",np.mean(students,axis=0))
print("Highest marks: ",np.max(students))
print("Lowest marks: ",np.min(students))


# Random normal distribution
scores = rng.normal(
    loc=70,
    scale=10,
    size=1000
)
print("Scores: ",scores)
print(scores.mean())
print(scores.std())

#Random choice :
posts = np.array(["Coder","tech","doctor","mechanic","engineer"])
print("Random choice: ",rng.choice(posts,size=5))

# Random shuffle array:
num = np.array([1,2,3,4,5])
print("array: ",num)
rng.shuffle(num)
print("shuffled array: ",num)
