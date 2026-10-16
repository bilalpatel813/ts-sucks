import pandas as pd

from pathlib import Path
DATA_DIR = Path(__file__).resolve().parents[2] / "data"
OUTPUT_DIR = Path(__file__).resolve().parents[2] / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
# - load data from csv
df = pd.read_csv(DATA_DIR / "creators.csv")

# - summarize statictics for every creator

report  = df.groupby("platform").agg(
    creator_count =("creator","count"),
    total_follower =("followers","sum"),
    average_follower=("followers","mean"),
    total_likes=("likes","sum"),
    average_likes=("likes","mean"),
    total_views=("views","sum"),
    average_views=("views","mean")
)

# - platform with the most total views 

report = report.sort_values(
    "total_views",
    ascending=False
)

print("Platform Analytics report: \n",report)

# -  save to csv file

report.to_csv(OUTPUT_DIR / "platform_analytic.csv")
print("report saved to platform_analytics.csv")

