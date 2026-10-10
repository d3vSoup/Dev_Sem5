import pandas as pd
import numpy as np

data = {
    'Emp_ID': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'YOE': [3, np.nan, 5, np.nan, 2, np.nan, 7],
    'Salary': [50000, 60000, np.nan, 0, 45000, np.nan, 80000],
    'Address': ['Delhi', np.nan, 'Mumbai', np.nan, 'Pune', np.nan, 'Delhi'],
    'Phone': ['9876543210', np.nan, np.nan, '9123456780', np.nan, np.nan, '9988776655']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)


# 1. Drop all rows with any missing value
ans1 = df.dropna()
print("\n--- 1. Drop all rows with any missing value ---")
print(ans1)


# 2. Salary is critical: Drop all rows missing Salary
ans2 = df.dropna(subset=['Salary'])
print("\n--- 2. Drop all rows missing Salary ---")
print(ans2)


# 3. Drop rows with > 2 missing values across any column
ans3 = df.dropna(thresh=len(df.columns) - 2)
print("\n--- 3. Drop rows with > 2 missing values ---")
print(ans3)
#what can be easier way of doing this ?



# 4. Address and Phone have many missing values... drop these columns wholly
ans4 = df.drop(columns=['Address', 'Phone'])
print("\n--- 4. Drop Address and Phone columns wholly ---")
print(ans4)


# 5. Drop rows that have YOE missing and Salary is missing or 0
drop_condition = df['YOE'].isna() & ((df['Salary'].isna()) | (df['Salary'] == 0))
ans5 = df[~drop_condition]
print("\n--- 5. Drop rows with YOE missing and Salary is missing or 0 ---")
print(ans5)
