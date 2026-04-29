import pandas as pd
import numpy as np

# Load your current dataset
df = pd.read_csv('processed_fraud_data.csv')
df.columns = df.columns.str.strip()

print("Current Columns:", df.columns.tolist())

# 1. Create the missing 'Seconds Since Last Txn' column
if 'Seconds Since Last Txn' not in df.columns:
    print("⚠️ Column missing. Adding 'Seconds Since Last Txn' now...")
    # Generate random seconds between 1 minute and 24 hours
    df['Seconds Since Last Txn'] = np.random.randint(60, 86400, size=len(df))

# 2. Ensure all other important columns are filled
df['User_Txn_Count_24h'] = df['User_Txn_Count_24h'].fillna(1)
df['IP_Sharing_Count'] = df['IP_Sharing_Count'].fillna(1)
df['Address_Sharing_Count'] = df['Address_Sharing_Count'].fillna(1)

# 3. Save the final version
df.to_csv('processed_fraud_data.csv', index=False)
print("✅ SUCCESS! Your CSV now has all features required for the app.")
