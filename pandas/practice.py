import pandas as pd 

df = pd.read_csv("ts-sucks/pandas/creators.csv")

# - display only followers and creator 
df = pd.read_csv("ts-sucks/pandas/creators.csv",usecols=["creator","followers"])
print("selected by creators ,followers:\n",df)
# - creator with followers more than 1500
print("Creators with followers greater than 1500:\n",df[df["followers"]>1500])
# - Creator with atleast 200 likes
df = pd.read_csv("ts-sucks/pandas/creators.csv")
print("Creator with atleast 200: \n",df[df["likes"]>200])

# - creator wiht 3000 - 10,000 views
print("creator with 3000 - 10,000 views:\n",df[df["views"].between(3000,10000)])

# - creator wiht highest like first
print("Creator with highest likes:\n",df.sort_values(by="likes",ascending=False))

# - top 2 creator by views
print("Top 2 creator by highest views:\n",df.nlargest(2,"views"))

# - save creator wiht atleast 2000 followers in csv
res = df[df["followers"]>2000]
save_res = res.to_csv("ts-sucks/pandas/top_creator.csv",index=False)
