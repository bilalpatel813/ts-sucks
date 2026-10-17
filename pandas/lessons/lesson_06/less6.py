import pandas as pd
import numpy as np

df = pd.DataFrame({
    "creator": ["Asha", "Rahul", "Sara", "Imran"],
    "followers": [1000, 2000, 5000, 0],
    "likes": [100, 300, 800, 50],
    "comments": [10, 30, 100, 5],
    "shares": [5, 20, 50, 5]
})

print(df)

# - vectorization df columns
df["interactions"] = df["likes"] + df["comments"] + df["shares"]
print(df[["creator","interactions"]])

df["engagement_rate"] = (df["interactions"]
                         .div(df["followers"].replace(0,np.nan))
                         .mul(100)
                         .round(2)
                         )
print(df[["creator","engagement_rate"]])

df["engagement_level"] = df["engagement_rate"].apply(lambda x:"Unknown" if pd.isna(x) else "High" if x>=15 else "Normal")
print(df[["creator", "engagement_rate", "engagement_level"]])

df["creator_type"] = np.where(
    df["followers"] >= 2000,
    "Established",
    "Growing"
)

print(df[["creator", "followers", "creator_type"]])

houses = pd.DataFrame({
    "area_sqft": [600, 1200, 2000],
    "price": [3_000_000, 8_000_000, 15_000_000]
})

houses["category"] = np.where(
    houses["price"] >= 10_000_000,
    "Expensive",
    "Other"
)

print(houses)

conditions =[
    houses["price"]< 5_00_000,
    houses["price"].between(5_00_000,10_00_000)
]
choices = [
    "Budget",
    "Mid-Range"
]
houses["price_group"] = np.select(
    conditions,
    choices,
    default="Premium"
)
print(houses[["price","price_group"]])





