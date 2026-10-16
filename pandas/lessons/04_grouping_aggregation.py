from pathlib import Path
import pandas as pd

data = {
    "creator": ["Rahul", "Aisha", "Aman", "Sara", "Neha", "Zoya"],
    "platform": [
        "Instagram", "Instagram", "YouTube",
        "Instagram", "YouTube", "Instagram"
    ],
    "content_type":["Education","fitness","tech",
                    "gaming","Doctor","Trade"],
    "followers": [1200, 2500, 800, 5000, 3200, 1800],
    "likes": [150, 340, 90, 720, 410, 220],
    "views": [3000, 7000, 2000, 15000, 9000, 4500]
}

df = pd.DataFrame(data)

print(df)

# - groupby & aggregation
groups = df.groupby("platform")
print(groups["followers"].sum())
print(df.groupby("platform")["views"].mean()) # average like form both platform
print(df.groupby("platform")["views"].max()) 
print(df.groupby("platform")["views"].min())
print("Creator in ",df.groupby("platform")["creator"].count()) # count the creator in every platform 
print(df.groupby("platform")["creator"].size())
print(df.groupby(["platform","content_type"])["views"].mean()) # gives average likes
# - agg()

result = df.groupby("platform")["followers"].agg(["sum","min","max","mean","count"])
print("result: \n",result)

summary = df.groupby("platform").agg(
    total_followers=("followers", "sum"),
    average_followers=("followers", "mean"),
    highest_followers=("followers", "max"),
    total_likes=("likes", "sum"),
    average_views=("views", "mean"),
    creator_count=("creator", "count")
)

print(summary)

top_creator  = df.sort_values("likes",ascending=False)
print(top_creator[["creator", "views"]].head(3))

idx = df.groupby("platform")["views"].idxmax()
top_by_platform = df.loc[
    idx,["creator","platform","views"]
]

print(top_by_platform)
