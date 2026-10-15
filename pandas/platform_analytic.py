import pandas as pd

# - load data from csv
df = pd.read_csv("ts-sucks/pandas/creators.csv")

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

report.to_csv("ts-sucks/pandas/platform_analytic.csv")
print("report saved to platform_analytics.csv")

