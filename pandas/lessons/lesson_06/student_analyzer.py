import pandas as pd

from pathlib import Path
DATA_DIR = Path(__file__).resolve().parents[2] / "data"
OUTPUT_DIR = Path(__file__).resolve().parents[2] / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
data ={
  "Name":["Bilal","Adnan","Gani","Obaid","Faiz"],
  "Python":[50,49,45,40,39],
  "Java":[50,40,35,37,30],
  "DSA":[45,40,40,30,25]
}
df = pd.DataFrame(data)

subjects = ["Python","Java","DSA"]
df["Average"] = df[subjects].mean(axis=1)
print("Average of all students:")
print(df)
print("-------------------------------")
df["Result"] = df["Average"].apply(
  lambda score: "Pass" if score>=20 else "Fail"
)
print("students Pass or Fail?")
print(df)
print("-------------------------------")
print("Highest Performer: ")
df = df.sort_values("Average",ascending=False)
print(df)
print("-------------------------------")
print("Full Report:")
print(df)
print("Class Average:")
print(df["Average"].mean())
print("Students Performed above 40: ")
print(df[df["Average"]>=40])
print("Top student: ",df.iloc[0])



