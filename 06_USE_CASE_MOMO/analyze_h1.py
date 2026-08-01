import pandas as pd
import glob
import re

file = "/Users/hienhv/Downloads/[TELCO-SIM] _ Inbound Report_ESIM Du lịch_Table.csv"
df = pd.read_csv(file)
# clean column names
df.columns = [c.strip() for c in df.columns]
# Sum total users
df['Total users'] = pd.to_numeric(df['Total users'], errors='coerce').fillna(0)

print(f"Total rows: {len(df)}")
print(f"Total users sum: {df['Total users'].sum()}")

# Print top 5 pages
print("\nTop 5 Pages:")
print(df.head(5).to_string(index=False))

file2 = "/Users/hienhv/Downloads/[TELCO-SIM] _ Inbound Report_ESIM Du lịch_Table (1).csv"
df2 = pd.read_csv(file2)
print(f"\nTotal queries: {len(df2)}")
print("Top 5 Queries (Position 1):")
print(df2[df2['Average Position'] == 1].head(5).to_string(index=False))
