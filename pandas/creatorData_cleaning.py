import pandas as pd

 # - load data from csv 
df = pd.read_csv("ts-sucks/pandas/creators.csv")

# - clean columns names

df.columns = (df.columns
              .str.strip()
              .str.lower()
              .str.replace(" ","_",regex =False)
              )

# - clean text columns
for column in ["creator","platform"]:
    if column in df.columns:
        df[column] = df[column].astype("string").str.strip()
if "platform" in df.columns:
    df["platform"]  = df["platform"].str.title()


# - clean numric data safely

for column in ["followers","likes","views"]:
    if column in df.columns:
        df[column]=pd.to_numeric(df[column],errors="coerce")

# - removes rows without creator names

if "creator" in df.columns:
    df = df.dropna(subset=["creator"])
    df= df[df["creator"] != ""]
    
# - removes fully duplicated rows
df = df.drop_duplicates()
# - Inspect missing values
print("Missing values: \n",df.isna().sum())

# - save cleaned data
df.to_csv("ts-sucks/pandas/creatorData_cleaned.csv")

print("Cleaning Completed")
print(df.head())


