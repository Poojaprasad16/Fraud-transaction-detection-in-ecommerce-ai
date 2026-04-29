import pandas as pd

# Load your processed dataset
df = pd.read_csv('processed_fraud_data.csv')

# Filter for IDs with high velocity (User_Txn_Count_24h > 5)
bot_ids = df[df['User_Txn_Count_24h'] > 5].head(5)

print("\n--- 🤖 USE THESE IDs TO DEMO THE BOT FEATURE ---")
if not bot_ids.empty:
    for index, row in bot_ids.iterrows():
        print(f"ID: {row['Transaction ID']} | Velocity: {row['User_Txn_Count_24h']}")
else:
    print("No high-velocity IDs found in the initial records.")
