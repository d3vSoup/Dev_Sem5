import pandas as pd
import numpy as np
# any upload .js or .csv is done via pandas

data = {
    'Name': ['Anu', 'Ravi', 'Meena', 'Kiran'],
    'Age': [20, 21, np.nan, 22],
    'Marks': [85, np.nan, 90, 65]
}
#np.nan is used to define missing values / null values. simple
#               'Age': [20, 21, np.nan, 22],
# to dinf the missing values and print them use 





# Create a DataFrame (which is the perfect way to represent tables in Python)
students_df = pd.DataFrame(data)
print("students\n")
print(students_df.isnull())
print(students_df.isnull().sum())
print(students_df.to_string(index=False))

#dropna is used to clean the missing value column only 
print()
students_df.dropna(subset=['Age', 'Marks'], inplace=True)
print(students_df.to_string(index=False))

# OR

#can i handle missing value using mean .. how ?
# if i k mean then i g we can get the missing value 
# lets just try it out 
mean_age = students_df['Age'].mean()
mean_marks = students_df['Marks'].mean()
students_df['Age'].fillna(mean_age, inplace=True)
students_df['Marks'].fillna(mean_marks, inplace=True)
print(students_df.to_string(index=False))







#csv file upload er jonne its pd. read_csv
# better yet is that we can upload the csv file from downloads section as 
file_path = '/Users/rik_mac/Downloads/students.csv'
df = pd.read_csv(file_path)
print(df)



#tgeres also drop_duplicates
#what does drop_duplicates do ? 

data2 = {
    'Name': ['Anu', 'Ravi', 'Meena', 'Kiran', 'Ravi'],
    'Age': [20, 21, 19, 22, 21],
    'Marks': [85, 72, 90, 65, 72]
}

students_df = pd.DataFrame(data2)
print("students\n")
print(students_df)
print(students_df.duplicated())
print(students_df.duplicated().sum())
students_df.drop_duplicates(inplace=True)
print(students_df.to_string(index=False))
