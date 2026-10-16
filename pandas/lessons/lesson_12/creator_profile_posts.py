import pandas as pd

from pathlib import Path
DATA_DIR = Path(__file__).resolve().parents[2] / "data"
OUTPUT_DIR = Path(__file__).resolve().parents[2] / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
# - load the csv files
creator = pd.read_csv(DATA_DIR / "creator.csv")
posts = pd.read_csv(DATA_DIR / "posts.csv")

# combine post with creator 
combined = pd.merge(posts,creator,on="creator_id",how="left",validate="many_to_one")

#  summarize posts performance by creator 
report = combined.groupby(["creator_id","creator","platform"],as_index=False).agg(
    total_posts=("post_id", "count"),
    total_likes=("likes", "sum"),
    average_likes=("likes", "mean"),
    total_views=("views", "sum"),
    average_views=("views", "mean")
)

# sort creator by total views
report = report.sort_values(
    "total_views",
    ascending=False
)

# save to csv file
report.to_csv(OUTPUT_DIR / "creator_report.csv",index=False)
print(report)
print("Saved creator_report.csv")
