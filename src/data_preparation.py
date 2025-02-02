import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("banking_transactions.csv")

# Convert timestamp column to datetime
df["Transaction_Timestamp"] = pd.to_datetime(df["Transaction_Timestamp"])

# Normalize Transaction Amount
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df["Transaction_Amount"] = scaler.fit_transform(df[["Transaction_Amount"]])

# Save cleaned dataset
df.to_csv("cleaned_transactions.csv", index=False)
print("Data preprocessing complete. Cleaned data saved as 'cleaned_transactions.csv'.")
