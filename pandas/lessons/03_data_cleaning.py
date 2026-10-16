from pathlib import Path
import pandas as pd

data = {
    "creator": [" @Rahul ", "Aisha", "Aman", "Aisha", None, "Neha"],
    "platform": ["Instagram", "Instagram", "YouTube",
                 "Instagram", "YouTube", " YouTube "],
    "followers": ["1200", "2500", None, "2500", "800", "3200"],
    "likes": [150, 340, 90, 340, None, 410],
    "post_date": ["2026-01-10", "2026-02-15", "invalid",
                  "2026-02-15", "2026-03-01", "2026-04-20"]
}

df = pd.DataFrame(data)

print(df)
print(df.isna()) # find missing values displays True for missing 

print(df.isna().sum()) # counts missing values
df["likes"] = df["likes"].fillna(0)
print(df)
df_clean = df.dropna(subset=["creator"]) # - removes full row of that missing values
print(df_clean) 

# - handling duplicates
print("--------------------------------")
print(df.duplicated())
print(df.duplicated().sum())
df  = df.drop_duplicates() # remove the row of the duplicated values 
print(df)

# - fix incorrect dtypes
print(df.dtypes)
df["followers"] = pd.to_numeric(df["followers"],errors="coerce")
print(df)
print(df.dtypes)
df["creator"]=df["creator"].str.strip()
df["platform"]=df["platform"].str.strip()

df["creator"]=df["creator"].str.replace("@","",regex=False)
print(df)


# - comvert and clean dates
print("---------------------------------")
print(df["post_date"].dtype)
df["post_date"]=pd.to_datetime(df["post_date"],errors="coerce") # - convert date object -> time
print(df["post_date"].dtype)
df["year"] = df["post_date"].dt.year

df["month"] = df["post_date"].dt.month
print(df)