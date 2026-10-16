import pandas as pd

from pathlib import Path
DATA_DIR = Path(__file__).resolve().parents[2] / "data"
OUTPUT_DIR = Path(__file__).resolve().parents[2] / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(DATA_DIR / "creators.csv")

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

leaderboard.to_csv(OUTPUT_DIR / "creator_leaderboard.csv",index=False)

print("Saved in creator_leaderboard.csv file!")

