import pandas as pd
import random
import numpy as np

df = pd.read_csv('processed_fraud_data.csv')
df.columns = df.columns.str.strip()

def fill_empty(column_name, min_val, max_val):
    if column_name in df.columns:
        df[column_name] = df[column_name].apply(
            lambda x: random.randint(min_val, max_val) if pd.isna(x) or x == "" or x == 0 else x
        )

fill_empty('User_Txn_Count_24h', 1, 15)
fill_empty('Seconds Since Last Txn', 60, 86400)
fill_empty('IP_Sharing_Count', 1, 10)
fill_empty('Address_Sharing_Count', 1, 5)

df.to_csv('processed_fraud_data.csv', index=False)
print("CSV Updated Successfully!")
