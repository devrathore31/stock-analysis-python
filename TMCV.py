import pandas as pd

CSV_FILE = "TMCV_stock_data.csv"

df = pd.read_csv(CSV_FILE, sep=",")

df.columns = df.columns.str.strip()

df["Close Price"] = df["Close Price"].astype(str).str.replace(",", "").str.strip()
df["Close Price"] = pd.to_numeric(df["Close Price"], errors="coerce")

max_close = df["Close Price"].max()
max_row = df[df["Close Price"] == max_close].iloc[0]

print("=" * 45)
print(f"  Stock         : {max_row['Symbol'].strip()}")
print(f"  Highest Close : Rs {max_close:.2f}")
print(f"  Date          : {max_row['Date'].strip()}")
print("=" * 45)