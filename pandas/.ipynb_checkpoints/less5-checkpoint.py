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
    "views": [3000, 7000, 4500, 2000],
#    "platform":["Instagram", "Instagram", "YouTube","Youtube"]
})
creators.to_csv("ts-sucks/pandas/creator.csv")
posts.to_csv("ts-sucks/pandas/posts.csv")

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
# - Stack rows vertically
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

# - join()
creator_profile = creators.set_index("creator_id")

creator_stats = pd.DataFrame({
    "followers": [1200, 2500, 800],
    "engagement_rate": [4.5, 6.2, 3.1]
},index=pd.Index([1,2,3],name="creator_id"))

print(creator_profile.join(creator_stats,how="left"))

print(pd.merge(posts,creators,on="creator_id",suffixes=("_posts","_creator"))) # suffixes the same column of both df

print("creator_id is uniques=",creators["creator_id"].is_unique)

print(pd.merge(posts,creators,on="creator_id",how="left",validate="many_to_one"))
