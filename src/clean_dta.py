import pandas as pd
df = pd.read_csv('data/sales.csv')
df["revenue"] = df["quantity"] * df["price"]
print(df)
