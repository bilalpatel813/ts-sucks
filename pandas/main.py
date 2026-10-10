import pandas as pd

df1 = pd.read_csv("sales-dataset/sales_data_dictionary.csv") 
df2 = pd.read_json("frontier-ai-datatset/models.json")
print(df1)
print(df2)