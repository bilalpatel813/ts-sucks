import pandas as pd

from pathlib import Path
DATA_DIR = Path(__file__).resolve().parents[2] / "data"
OUTPUT_DIR = Path(__file__).resolve().parents[2] / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
 # - load data from csv 
df = pd.read_csv(DATA_DIR / "creators.csv")

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
df.to_csv(OUTPUT_DIR / "creatorData_cleaned.csv")

print("Cleaning Completed")
print(df.head())


