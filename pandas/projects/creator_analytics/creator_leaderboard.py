from pathlib import Path
import pandas as pd

df = pd.read_csv((Path(__file__).resolve().parents[2] / "data" / "raw" / "creators.csv"))

#-  Inpsect the data
print("data shape: ",df.shape)
print("First Five Rows:\n",df.head())

# - Find Creator with atleast 1000 follower
eligible = df[df["followers"]>1000]

#- Calculate likes per 1000 views

eligible  = eligible.copy()
eligible["likes_per_1000_views"] = (eligible["likes"] / eligible["views"] *1000)

# - sort by  followers highest first 
leaderboard = eligible.sort_values(by="followers",ascending=False)

# - display selected columns

print("\nCreator LeaderBoard:")
print(leaderboard[["creator","followers","likes","views","likes_per_1000_views"]])

# - save in files 

leaderboard.to_csv((Path(__file__).resolve().parents[2] / "data" / "processed" / "creator_leaderboard.csv"),index=False)

print("Saved in creator_leaderboard.csv file!")

