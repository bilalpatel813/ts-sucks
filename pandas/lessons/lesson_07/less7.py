import pandas as pd
stocks = pd.DataFrame({
    "date": [
        "2026-10-15", "2026-10-15",
        "2026-10-16", "2026-10-16",
        "2026-10-17", "2026-10-17"
    ],
    "company": [
        "TCS", "Infosys",
        "TCS", "Infosys",
        "TCS", "Infosys"
    ],
    "close": [3200, 1500, 3250, 1520, 3230, 1550]
})

stocks["date"] = pd.to_datetime(stocks["date"])

stocks = stocks.set_index(["date", "company"]).sort_index()

print(stocks)

print("TCS on 15 Oct:\n",stocks.loc[(pd.Timestamp("2026-10-15"),"TCS")])

print("company's on 16 oct:\n",stocks.loc[pd.Timestamp("2026-10-16")])
print(stocks.xs("TCS",level="company"))

creators = pd.DataFrame({
    "date": [
        "2026-10-15", "2026-10-15",
        "2026-10-16", "2026-10-16"
    ],
    "creator": ["Aisha", "Rahul", "Aisha", "Rahul"],
    "views": [2500, 4000, 3000, 4500],
    "likes": [250, 400, 330, 420]
})

creators["date"] = pd.to_datetime(creators["date"])

creators = (
    creators
    .set_index(["date", "creator"])
    .sort_index()
)

print(creators.loc[pd.Timestamp("2026-10-16")])




