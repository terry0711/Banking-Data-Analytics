import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_transactions.csv")

# Fraud vs Non-Fraud Transactions
plt.figure(figsize=(6,4))
sns.countplot(x="Is_Fraud", data=df, palette="coolwarm")
plt.title("Fraud vs Legit Transactions")
plt.xlabel("Transaction Type (0 = Legit, 1 = Fraud)")
plt.ylabel("Count")
plt.show()

# Spending Trends by Merchant Category
plt.figure(figsize=(10,5))
sns.boxplot(x="Merchant_Category", y="Transaction_Amount", data=df, palette="Set2")
plt.title("Transaction Amount Distribution by Merchant Category")
plt.xticks(rotation=45)
plt.show()

# Fraud Cases by Location
fraud_by_location = df[df["Is_Fraud"] == 1]["Location"].value_counts()
plt.figure(figsize=(8,4))
sns.barplot(x=fraud_by_location.index, y=fraud_by_location.values, palette="mako")
plt.title("Fraud Cases by Location")
plt.xlabel("City")
plt.ylabel("Number of Fraud Cases")
plt.show()

print("EDA complete. Visualizations generated.")
