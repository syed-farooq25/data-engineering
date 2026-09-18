import pandas as pd

df = pd.read_csv("messy_loans.csv")

print("--- Raw data ---")
print(df)

print("\n--- Data types ---")
print(df.dtypes)

df["status"] = df["status"].str.lower()
df["customer_name"] = df["customer_name"].str.strip()
df["amount"] = df["amount"].fillna(0)

print("\n--- After cleaning ---")
print(df)

df.to_csv("clean_loans.csv", index=False)
print("\nSaved cleaned data to clean_loans.csv")