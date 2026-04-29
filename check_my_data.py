import pandas as pd

df = pd.read_csv('processed_fraud_data.csv')

# 1. Clean all column names by stripping hidden spaces
df.columns = df.columns.str.strip()

# 2. Check if a column looks like the 'Seconds' one but has a slightly different name
# If it finds 'Seconds Since Last Txn' or similar, it renames it to exactly 'Seconds Since Last Txn'
for col in df.columns:
    if 'Seconds' in col and 'Last' in col:
        df.rename(columns={col: 'Seconds Since Last Txn'}, inplace=True)
        print(f"✅ Renamed '{col}' to 'Seconds Since Last Txn'")

# 3. Fill any remaining blanks just in case
df['Seconds Since Last Txn'] = df['Seconds Since Last Txn'].fillna(0).replace('', 0)

# 4. Save it back
df.to_csv('processed_fraud_data.csv', index=False)
print("🚀 Data is now 100% synchronized with your App!")