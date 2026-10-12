import pandas as pd 

df = pd.read_csv("ts-sucks/pandas/creators.csv")

# - display only followers and creator 
df = pd.read_csv("ts-sucks/pandas/creators.csv",usecols=["creator","followers"])
print("selected by creators ,followers:\n",df)
# - creator with followers more than 1500
print("Creators with followers greater than 1500:\n",df[df["followers"]>1500])

