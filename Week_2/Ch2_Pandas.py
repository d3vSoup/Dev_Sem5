import pandas as pd
import numpy as np

# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a 
# table with rows and columns.
data = {
    'Emp_ID': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'YOE': [3, np.nan, 5, np.nan, 2, np.nan, 7],
    'Salary': [50000, 60000, np.nan, 0, 45000, np.nan, 80000],
    'Address': ['Delhi', np.nan, 'Mumbai', np.nan, 'Pune', np.nan, 'Delhi'],
    'Phone': ['9876543210', np.nan, np.nan, '9123456780', np.nan, np.nan, '9988776655']
}

#load data into DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

#named indexing - when rows and column have name (labels) instead of numbers (integers) .. 
# it uses label to select rows and columns
# to use named indexing .. we use .loc[]

df=pd.dataFrame(data,index=["emp1","emp2","emp3","emp4","emp5","emp6","emp7"])  
print("\n--- Named Indexing ---")
print(df.loc["emp1"])
print(df.loc[["emp1", "emp2"]])


#load files ( eg. data.csv ) into table 
df = pd.read_csv("data.csv")

# f() s
'''

merge()          for combining data on common columns or indices
join()           is used to combine two DataFrames on the index but not on columns
concat()         for combining DataFrames across rows or columns





                   Concat () combining data across rows or columns 
                        • With concatenation, your datasets are just stitched together along an axis — either the row axis or column axis

                            • axis represents the axis that you’ll concatenate along. The default value is 0, which concatenates along the index, or row axis. Alternatively, a value of 1 will concatenate vertically, along columns. You can also use the string values "index" or "columns"
                            • Ignore_index takes a Boolean True or False value. It defaults to False. If True, then the new combined dataset won’t preserve the original index values in the axis specified in the axis parameter. This lets you have entirely new index values. 

                            dataframe = pd.concat([dataFrame1, dataFrame2, dataFrame3],ignore_index=True,axis=0)








                   merge() function
                        • Merge is one of the most powerful functions in pandas for combining data. It is used to combine two DataFrames on the basis of a common column or index.
                        • The function is used to perform database-style joins and merges.
                        • Pandas merges two DataFrames based on common keys present in both DataFrames
                        • The keys can be column values or indices.
                        • It can be used to perform various types of joins such as inner join, outer join, left join, and right join. ( defaults to inner join,other possible options include 'outer', 'left', and 'right' )
                        • It can also be used to perform conditional joins.
                        • It can also be used to merge multiple DataFrames.
                        • It can also be used to merge DataFrames with different column names.

                        on tells merge() which columns or indices, also called key columns or key indices, you want to join on.
                        left_on and right_on are used to merge DataFrames with different column names.


                        df1=pd.DataFrame({"id": [1,2,3,4,5], "name": ["A","B","C","D","E"], "age": [25,26,27,28,29]})
                        df2=pd.DataFrame({"id": [1,2,3,4,5], "city": ["Delhi","Mumbai","Kolkata","Chennai","Hyderabad"]})
                        print(df1)
                        print(df2)

                        df3=pd.merge(df1,df2,on="id",how="inner")
                        print(df3)
                        df3=pd.merge(df1,df2,on="id",how="outer")
                        print(df3)
                        df3=pd.merge(df1,df2,on="id",how="left")
                        print(df3)
                        df3=pd.merge(df1,df2,on="id",how="right")
                        print(df3)


                        The inner join takes the intersection from two or more dataframes. It corresponds to the INNER JOIN in Structured Query Language (SQL).
                        easier way to remember : common elements of two dataframes

                        The outer join takes the union from two or more dataframes. It corresponds to the FULL OUTER JOIN in SQL.
                        easier way : common and uncommon elements of two dataframes.. IMPORTANT.. ALWAYS PRESERVE KEYS OF BOTH TABLES

                        The left join uses the keys from the left-hand dataframe only. It corresponds to the LEFT OUTER JOIN in SQL.
                        easier way : common and uncommon elements of two dataframes but prioritising left hand dataframe

                        The right join uses the keys from the right-hand dataframe only. It corresponds to the RIGHT OUTER JOIN in SQL.
                        easier way : common and uncommon elements of two dataframes but prioritising right hand dataframe
                        

                    Merging on index : 
                    df1=pd.DataFrame({"A": [1,2,3,4,5], "name": ["A","B","C","D","E"]})
                    What it does : is the default way of merging like we can merge using indexes by using on="index"
                    left 1 = pd.dtaFrame ({ 'key':[1,2,3], 'value1':['A','B','C']})
                    right 1 = pd.dtaFrame ({ 'key':[1,2,3], 'value2':['A','B','C']}) 
                    pd.merge(left1,right1,on="key",how="inner")


                    'value' : range(6) what it does ? It creates a sequence of 6 values from 0 to 5 which are 0,1,2,3,4,5 and assigns them to value column 
                    

                    if said... merge 2 DF with columns matching ... iner
                    if said.. merge 2 DF with columns records of both sides where available ... outer







                        join() : Combine DF on the index 

                        lsuffix: Suffix to be used for overlapping column names in left dataframe (default: '_left')
                        rsuffix: Suffix to be used for overlapping column names in right dataframe (default: '_right')

                        
                        
                        




                        append() - dataframe.append() - appends rows of 2nd to first ... 
                                Columns not in the original data frames are added as new columns and the new cells are populated with NaN value 

                        
                        df1 = pd.DataFrame({'A': ['a', 'b'], 'B': [1, 2]})
                        df2 = pd.DataFrame({'B': [3, 4], 'C': ['c', 'd']})
                        df1.append(df2, ignore_index=True)
                        
                        
                        rows= default...  ... concart along Rows.
                        column = axis = 1... we use this to concat along columns 
                    

                        

'''








# Data deduplication 
 # Data deduplication involves identifying and removing redundant records to ensure dataset cleanliness and analysis accuracy.

frame3 = pd.DataFrame({
    'column 1': ['Looping'] * 3 + ['Functions'] * 4,
    'column 2': [10, 10, 22, 23, 23, 24, 24]
})
 # In this dataset, rows 0 and 1 are identical ('Looping', 10), rows 3 and 4 are identical ('Functions', 23), and rows 5 and 6 are identical ('Functions', 24).

# duplicated() method scans the DF and returns a Boolean Series of the same length to identify duplicates
frame3.duplicated()  
'''
False: The first time a distinct combination of values appears.   
True: Any subsequent occurrence of an already-seen row.   
Executing frame3.duplicated() returns True for index positions 1, 4, and 6. 

'''
# remove dupes with drop_duplicates().. returns cleaned DF 
frame4 = frame3.drop_duplicates()
'''
frame4 retains only index positions 0, 2, 3, and 5. By default, both duplicated() and drop_duplicates() preserve the first 
observed occurrence of a duplicate entry. 

IMP: 
take_last=True or last='True'      preserves the last occurrence instead.

'''

#advanced detection across Columns

'''
Filtering Syntax
        To view the actual duplicated records rather than just a Boolean mask, 
        Boolean indexing is applied:   
        
                Across all columns: df[df.duplicated()]   
                Across specific columns: df[df.duplicated(['col1', 'col2'])]   


            df = pd.DataFrame({
                                'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                                'points': [10, 10, 12, 12, 15, 17, 20, 20],
                                'assists': [5, 5, 7, 9, 12, 9, 6, 6]
                            })


df.[df.duplicated()]                                         checks for identical values across all columns ( check duplicate rows acxross all columns)
df[df.duplicated(subset=['team', 'points'])]                 checks for identical values across specific columns (check duplicate rows across ['team', 'points']) 

When deduplication should ignore certain fields (like variations in assists), subset columns are passed as a list:

duplicates = df[df.duplicated(['team', 'points'])]


dropping duplicates = 
df.drop_duplicates(subset=['team', 'points'], keep='first', inplace=True)

What is dropna ?
dropna --> drop na (not available).. in numpy its nan (not a number)

dropna(df) ... it drops rows/ columns with nan values

Example : 
'''



import numpy as np
import pandas as pd

df = pd.DataFrame({
    "City": ["Hyderabad", "Mumbai", "Delhi", "", "Kolkata", "Chennai"],
    "Sales": [250, 150, np.nan, 300, 120, 90],
    "Growth": [10.5, 12.2, 8.0, np.nan, 14.5, 11.0]
})

print("--- Original DataFrame ---")
print(df)

# 1. Drop rows with ANY NaN
rows_dropped = df.dropna()
print("\n--- After dropping rows with ANY NaN ---")
print(rows_dropped)


# 2. Drop columns with ANY NaN
columns_dropped = df.dropna(axis=1)
print("\n--- After dropping columns with ANY NaN ---")
print(columns_dropped)


# 3. Drop rows ONLY if ALL values are NaN (no effect here as no fully empty rows)
all_nan_dropped = df.dropna(how='all')
print("\n--- After dropping rows where ALL values are NaN ---")
print(all_nan_dropped)


# 4. Drop columns ONLY if ALL values are NaN (no effect here)
all_nan_columns_dropped = df.dropna(axis=1, how='all')
print("\n--- After dropping columns where ALL values are NaN ---")
print(all_nan_columns_dropped)


# 5. Drop rows with at least 2 NaNs
thresh_dropped = df.dropna(thresh=len(df.columns) - 2)
print("\n--- After dropping rows with at least 2 NaNs ---")
print(thresh_dropped)


# 6. Drop rows with missing values ONLY in specific columns (e.g., Sales)
subset_dropped = df.dropna(subset=['Sales'])
print("\n--- After dropping rows missing 'Sales' ---")
print(subset_dropped)









#replace (): 

# Datasets often use arbitrary numbers (such as -786 or -999) to denote 
# invalid or corrupted entries instead of standard null indicators. 
# The .replace() method locates and substitutes these values:

import numpy as np
import pandas as pd

replaceFrame = pd.DataFrame({
    'column 1': [200., 3000., -786., 3000., 234., 444., -786., 332., 3332.],
    'column 2': range(9)
})

# Replace sentinel value -786 with standard np.nan
clean_frame = replaceFrame.replace(to_replace=-786, value=np.nan)



#Presents a product catalog where entry index 3 has 'Veggie' recorded under the 'Category' column 
# instead of standardizing with 'Fruit':
data = {
    'Product_ID': [1, 2, 3, 4, 5],
    'Product_Name': ['Apple', 'Banana', 'Orange', 'Pear', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Veggie', 'Fruit']
}
df = pd.DataFrame(data)

#Q: How do you replace 'Veggie' with 'Fruit' in the 'Category' column using replace()?
df['Category'] = df['Category'].replace('Veggie', 'Fruit')
# Or across the entire DataFrame:
df.replace(to_replace='Veggie', value='Fruit', inplace=True)

















# drop na () stuff 
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
