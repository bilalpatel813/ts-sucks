import pandas as pd

df = pd.read_csv("ts-sucks/pandas/creators.csv")
print("data from csv file\n",df)
df =  pd.read_csv("ts-sucks/pandas/creators.csv",nrows=3)
print("first three rows :\n",df)
df =  pd.read_csv("ts-sucks/pandas/creators.csv",usecols=["creator","likes"])
print("gives only selected columns: \n",df)
df =  pd.read_csv("ts-sucks/pandas/creators.csv",index_col="creator")
print("creator as column: \n",df)

df = pd.read_json("ts-sucks/pandas/creators.json")
print("data from json file: \n",df)
print(df[["creator", "likes", "views"]])
print("gives first row:\n ",df.iloc[0])
print("gives rows and columns:\n",df.iloc[0:3,0:2])
result = df[df["likes"]>300]
print("gives user likes greater than 300\n",result)
res = df[(df["followers"]>2000)&(df["likes"]>300)]
print("givs users with at least 2,000 followers and at least 300 likes:\n",res)
res = df[~(df["platform"]=="youtube")]
print("gives creators who are not on YouTube:\n",res)
