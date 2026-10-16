import pandas as pd

df = pd.read_csv("ts-sucks/pandas/creators.csv")
print("data from csv file\n",df)
df =  pd.read_csv("ts-sucks/pandas/creators.csv",nrows=3)
print("first three rows :\n",df)
df =  pd.read_csv("ts-sucks/pandas/creators.csv",usecols=["creator","likes"])
print("gives only selected columns: \n",df)
df =  pd.read_csv("ts-sucks/pandas/creators.csv",index_col="creator")
print("creator as column: \n",df)
# - fetch via integers position 
df1 = pd.read_json("ts-sucks/pandas/creators.json")
print("data from json file: \n",df)
print(df1[["creator", "likes", "views"]])
print("gives first row:\n ",df1.iloc[0])
print("gives rows and columns:\n",df1.iloc[0:3,0:2])
# - conditional logic 
print("------------------------")
result = df1[df1["likes"]>300]
print("gives user likes greater than 300\n",result)
res = df1[(df1["followers"]>2000)&(df1["likes"]>300)]
print("givs users with at least 2,000 followers and at least 300 likes:\n",res)
res = df1[~(df1["platform"]=="youtube")]
print("gives creators who are not on YouTube:\n",res)
platforms = ["Instagram","Youtube"]
df1 = df1[df1["platform"].isin(platforms)]
print("fetching via platform name:\n",df1)
df1 = df1[df1["followers"].between(1000,3000)]
print("gives user which have followers 1000-3000\n",df1)

df = df.query("followers > 2000 and likes >300")
print(df)

mini_follower = 2000
print(df.query("followers > @mini_follower"))
# - sorting
print("-----------------------")
res = df.sort_values( by="followers",ascending=False)
print(res) # highest followers first 
res = df.sort_values(by="likes",ascending=True)
print(res) # lowest likes first
res = df.sort_values( by=["followers","likes"],
                     ascending =[False,True])

res = df.nlargest(3,"followers")
print("gives 3 users with highest follower:\n",res)
print("gives 3 user with low followers:\n",df.nsmallest(3,"followers"))

# - save results in new files

saved_csv = res.to_csv("ts-sucks/pandas/results.csv",index=False)
saved_json = res.to_json("ts-sucks/pandas/results.json",orient ="records",indent=2)

load_saves= pd.read_csv("ts-sucks/pandas/results.csv")
print("CSV Saved data:\n",load_saves)
load_saves = pd.read_json("ts-sucks/pandas/results.json")
print("Json Saved data:\n",load_saves)


