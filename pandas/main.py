import pandas as pd

marks  = pd.Series(
  [78,90,66,80,79,85],
  index=["Adnan","Bilal","Faiz","Obaid","Asif","Gani"]
)
print(marks)
print("average marks: ",marks.mean())
print("highest marks: ",marks.max())
print("lowest marks: ",marks.min())
print("total marks: ",marks.sum())
print("Bilal's marks: ",marks["Bilal"])
print("----------------------------")
data = {"Name":["Adnan","Bilal","Faiz","Obaid"],
        "Age":[18,18,18,10],
        "Class":["SYcs","SYcs","SYcs","SYcs"],
        "Marks":[78,90,66,80]
     }
df = pd.DataFrame(data)
print(df)
print(df.head()) # first 5 rows 
print(df.head(2)) 
print(df.tail()) # last 5 rows 
print("shape: ",df.shape)
#print(df.columns)
#print(df.dtypes)
print(df.info())
print(df.describe())

print(df["Age"])          # One column: Series
print(df[["Name", "Age"]]) # Multiple columns: DataFrame
print("--------------------------")
print(df.loc[0])
print(df.loc[1,"Name"])
print(df.iloc[0])
print(df.iloc[1,2])
print("--------------------------")
# filtering data with condition

print(df[df["Marks"]>=80])
result = df[
    (df["Age"] >= 17) &
    (df["Marks"] >= 85)
]

print(result)
print("---------------------------")
df["Passed"] = df["Marks"]>=40
df["Percentage"] = df["Marks"] /100 * 100
print(df)
df = df.rename(columns ={"Marks":"Score"})
df = df.drop(columns=["Age"])
print()
print(df)
