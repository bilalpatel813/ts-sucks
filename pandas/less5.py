import pandas as pd

creators = pd.DataFrame({
    "creator_id": [1, 2, 3],
    "creator": ["Rahul", "Aisha", "Aman"],
    "platform": ["Instagram", "Instagram", "YouTube"]
})

posts = pd.DataFrame({
    "post_id": [101, 102, 103, 104],
    "creator_id": [1, 2, 1, 3],
    "likes": [150, 340, 220, 90],
    "views": [3000, 7000, 4500, 2000]
})

print(creators)
print(posts)

result = pd.merge(
    posts,
    creators,
    on="creator_id"
)

print("innner:\n",pd.merge(posts, creators, on="creator_id", how="inner"))
print("left join:\n",pd.merge(posts, creators, on="creator_id", how="left"))
print("right:\n", pd.merge(posts, creators, on="creator_id", how="right"))
print("outer:\n",pd.merge(posts, creators, on="creator_id", how="outer"))
print("-------------------------")
print(pd.merge(posts,creators,left_on="creator_id",right_on="creator_id",how="left")) # merge same columns of both df

print("-------------------------")
# - Stsck rows vertically
january = pd.DataFrame({
    "post_id": [101, 102],
    "likes": [150, 340]
})

february = pd.DataFrame({
    "post_id": [103, 104],
    "likes": [220, 410]
})
all_post = pd.concat([january,february],ignore_index=True) # concatinates both the dataframes vertically
print(all_post)

# - combine columns horizontally
names = pd.DataFrame({
    "creator": ["Rahul", "Aisha", "Aman"]
})

followers = pd.DataFrame({
    "followers": [1200, 2500, 800]
})

combined = pd.concat([names,followers],axis=1,ignore_index=False)
print(combined)
