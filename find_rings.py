import pandas as pd

# Load your cleaned data
df = pd.read_csv('processed_fraud_data.csv')

# Find transactions where more than 5 people share an IP
fraud_rings = df[df['IP_Sharing_Count'] > 5].head(5)

print("\n--- 🕸️ USE THESE IDS FOR YOUR SPIDER-WEB GRAPH ---")
if not fraud_rings.empty:
    for index, row in fraud_rings.iterrows():
        print(f"ID: {row['Transaction ID']} | Users on this IP: {row['IP_Sharing_Count']}")
else:
    print("No high-sharing IDs found in the first few rows.")
