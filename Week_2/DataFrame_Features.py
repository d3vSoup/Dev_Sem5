# ==============================================================================
# PANDAS & NUMPY COMPLETE REVISION GUIDE (HUMAN & DESI MNEMONICS EDITION)
# ==============================================================================
# Yaad rakhne ka simple tareeka:
# 1. Duplicates Pakadna:  df.duplicated()
# 2. Duplicate Rule:       keep='first', keep='last', keep=False
# 3. Duplicate Hatana:     df.drop_duplicates()
# 4. Column vs Row Fanda:  Khada pillar (Column) vs Leta record (Row)
# 5. Naam Badalna:         df.rename(columns={'Purana': 'Naya'})
# 6. Sorting:              df.sort_values(by=...)
# 7. Filtering:            Bracket lagao: (cond1) & (cond2)
# 8. Badalna & Assign:     .replace(to_replace=Kisko, value=Kya), df['Naya'] = df['Purana']
# 9. Missing Data:         NaN sambhalna (isna, dropna, fillna, ffill, bfill)
# 10. NumPy Jugad:         arange (1 'r'!) aur reshape (Magic -1)
# ==============================================================================

import pandas as pd
import numpy as np

# Deprecation warning band karne ke liye option
pd.set_option('future.no_silent_downcasting', True)






# ==============================================================================
# 0. SAMPLE DATAFRAME (Hospital Patient Data - Bilkul Original & Unchanged)
# ==============================================================================
# Socho ek hospital ka register hai jisme 20 patients ka record hai:

data = {
    "Patient_ID": range(101, 121),

    "Age": [25, 40, 32, 28, 55, 45, 60, 35, 50, 29,
            38, 47, 22, 65, 41, 30, 52, 27, 58, 36],

    "Gender": ["Male", "Male", "Female", "Female", "Male",
               "Female", "Male", "Female", "Male", "Female",
               "Male", "Female", "Male", "Male", "Female",
               "Male", "Female", "Female", "Male", "Female"],

    "Disease": ["Fever", "Diabetes", "Asthma", "Fever", "Heart Disease",
                "Diabetes", "Hypertension", "Asthma", "Heart Disease", "Fever",
                "Diabetes", "Asthma", "Fever", "Hypertension", "Diabetes",
                "Heart Disease", "Fever", "Asthma", "Hypertension", "Diabetes"],

    "Department": ["General", "Medicine", "Pulmonary", "General", "Cardiology",
                   "Medicine", "Cardiology", "Pulmonary", "Cardiology", "General",
                   "Medicine", "Pulmonary", "General", "Cardiology", "Medicine",
                   "Cardiology", "General", "Pulmonary", "Cardiology", "Medicine"],

    "Days_Admitted": [2, 5, 3, 1, 7, 4, 6, 3, 8, 2,
                      5, 3, 2, 7, 4, 6, 2, 3, 5, 4],

    "Treatment_Cost": [5000, 15000, 10000, 3000, 25000,
                       12000, 20000, 9000, 30000, 4500,
                       14000, 8500, 4000, 22000, 13000,
                       24000, 5500, 9500, 18000, 11000],

    "Insurance": ["Yes", "Yes", "No", "No", "Yes",
                  "Yes", "No", "Yes", "Yes", "No",
                  "Yes", "No", "Yes", "Yes", "No",
                  "Yes", "No", "Yes", "Yes", "No"]
}

df = pd.DataFrame(data)

print("--- ORIGINAL DATAFRAME (Pehle 5 Rows) ---")
print(df.head())






# ==============================================================================
# 1. FINDING DUPLICATES: duplicated() -> "Duplicate pakdo!"
# ==============================================================================
# MNEMONIC & DESI LOGIC:
# * duplicated() ek CID inspector ki tarah hai.
# * Yeh har row ko check karta hai:
#     - False = "Yeh banda pehli baar aaya hai (Original/Unique)"
#     - True  = "Arrey yeh toh nakli duplicate hai! Dobara aaya hai."
# * Asli rows dekhne ke liye bahar df[...] laga do:
#     df[ df.duplicated(...) ]


# 1A. Poori row duplicate hai kya? (Across ALL columns)
# Yahan har patient ka ID alag hai (101 se 120), toh poori row kabhi duplicate nahi hogi.
print("\n--- 1A. Duplicates across ALL columns ---")
print("Total duplicate rows (sab columns mila kar):", df.duplicated().sum())


# 1B. Kisi ek specific column me duplicate dekhna:
# TRICK: subset=['Column_Name'] use karo!
# Matlab: "Bhai bas 'Disease' column me check kar kaunsi bimari repeat ho rahi hai."
print("\n--- 1B. Duplicate rows based on 'Disease' column ---")
dup_disease = df[df.duplicated(subset=['Disease'])]
print(dup_disease[['Patient_ID', 'Disease', 'Department']].head())


# 1C. N COLUMNS me duplicate check karna (Multi-Column Check):
# TRICK: subset=['Col1', 'Col2', ...] list pass karo!
# Matlab: "Dono match hone chahiye - Disease BHI aur Department BHI."
print("\n--- 1C. Duplicates across 2 columns ('Disease' + 'Department') ---")
dup_disease_dept = df[df.duplicated(subset=['Disease', 'Department'])]
print(dup_disease_dept[['Patient_ID', 'Disease', 'Department']].head())






# ==============================================================================
# 2. THE 'keep' PARAMETER: "Kisko rakhna hai aur kisko chor bolna hai?"
# ==============================================================================
# MNEMONIC (Simple yaad rakhne ka formula):
#
# 1. keep='first' (By Default) -> "Pehle aao, pehle paao"
#    Pehla banda asli (False), uske baad aane wale sab copycats (True).
#
# 2. keep='last'               -> "Aakhri bacha asli"
#    Aakhri wala banda asli (False), usse pehle wale sab copycats (True).
#
# 3. keep=False                -> "Dono chor hain!"
#    Kissi ko mat chhod! Jitni baar bhi repeat hua, sabhi rows ko True mark kar do.
#    (Inspection ke liye best hai jab saari duplicate copies ek saath dekhni hon).


print("\n--- 2A. keep='first' (Pehle wale ko original maano, baaki sab duplicate) ---")
print(df[df.duplicated(subset=['Disease'], keep='first')][['Patient_ID', 'Disease']].head(3))


print("\n--- 2B. keep='last' (Aakhri wale ko original maano, pehle wale duplicate) ---")
print(df[df.duplicated(subset=['Disease'], keep='last')][['Patient_ID', 'Disease']].head(3))


print("\n--- 2C. keep=False (Saari copies ko duplicate bolo) ---")
print(df[df.duplicated(subset=['Disease'], keep=False)][['Patient_ID', 'Disease']].head(6))






# ==============================================================================
# 3. DROPPING DUPLICATES: drop_duplicates() -> "Kachra saaf karo"
# ==============================================================================
# MNEMONIC:
# duplicated() sirf batata hai ki duplicate kaun hai.
# drop_duplicates() unhe seedha delete kar ke naya saaf dataframe deta hai!


# 3A. Ek column ke duplicate drop karna:
# "Disease column me se har bimari ka sirf 1 patient rakho, baaki hata do"
df_unique_disease = df.drop_duplicates(subset=['Disease'], keep='first')
print("\n--- 3A. drop_duplicates() on 'Disease' (Har bimari ka ek hi row bacha) ---")
print(df_unique_disease[['Patient_ID', 'Disease', 'Department']])


# 3B. Multiple columns ke combination pe drop karna:
# "Disease + Department ka unique joda rakho"
df_unique_disease_dept = df.drop_duplicates(subset=['Disease', 'Department'], keep='first')
print(f"\n--- 3B. Rows bache after dropping (Disease + Department): {len(df_unique_disease_dept)} ---")


# 3C. PRO-TIP: .reset_index(drop=True)
# Jab rows delete hoti hain, index number me gap aa jata hai (0, 2, 5...).
# reset_index se ginti wapas 0, 1, 2, 3 se shuru ho jaati hai:
df_clean = df.drop_duplicates(subset=['Disease']).reset_index(drop=True)






# ==============================================================================
# 4. COLUMN NAMES vs ROW NAMES / INDICES (KAB KYA USE KAREIN?)
# ==============================================================================
# ------------------------------------------------------------------------------
# DESI MNEMONIC:
#
# COLUMN = "Khada Pillar (Vertical Feature)"
#  -> Iska hamesha NAAM hota hai (jaise 'Age', 'Gender', 'Disease')
#  -> Kahan use hota hai?
#     1. Column chunna:         df['Age']  ya  df[['Age', 'Gender']]
#     2. Check karna:           subset=['Disease']
#     3. Sort karna:            df.sort_values(by='Age')
#     4. Rename karna:          df.rename(columns={'Purana': 'Naya'})
#     5. Filter lagana:         df[df['Age'] > 40]
#
# ROW = "Leta hua Record (Horizontal Patient)"
#  -> Iska hamesha INDEX / GINTI hoti hai (jaise row 0, row 1, row 2)
#  -> Kahan use hota hai?
#     1. .loc['label']   -> "L se Label" (Row ka naam ya index number se dhoondho)
#     2. .iloc[position] -> "I se Integer" (Row ki exact position 0, 1, 2 se dhoondho)
#     3. df.index.duplicated() -> "Row numbers duplicate toh nahi hain?"
#     4. df.drop(index=[0, 1]) -> "Row number 0 aur 1 ko hata do"
# ------------------------------------------------------------------------------


print("\n--- 4A. Row Access: .loc vs .iloc ---")
print("Row index 0 (.loc se):\n", df.loc[0, ['Patient_ID', 'Disease', 'Age']])

print("\nFirst 3 rows (.iloc se position 0 se 3):\n", df.iloc[0:3][['Patient_ID', 'Age']])


print("\n--- 4B. Duplicate Row Index Check ---")
print("Kya koi duplicate row index hai?:", df.index.duplicated().any())






# ==============================================================================
# 5. RENAMING COLUMNS: rename() -> "Purana Naam Hatake Naya Naam Dena"
# ==============================================================================
# MNEMONIC:
# Socho purana samaan dekar naya le rahe ho:
# columns = { 'Purana_Naam' : 'Naya_Naam' }

df_renamed = df.rename(columns={
    "Disease": "Condition",
    "Treatment_Cost": "Cost_INR"
})

print("\n--- 5. Renamed Columns ('Disease' -> 'Condition', 'Treatment_Cost' -> 'Cost_INR') ---")
print(df_renamed[['Patient_ID', 'Condition', 'Cost_INR']].head(3))






# ==============================================================================
# 6. SORTING: sort_values() -> "Line me khada karna (Chhota ya Bada)"
# ==============================================================================
# MNEMONIC:
# ascending=True  -> "Chhote se bada" (Seedhi upar chadhna: 1, 2, 3...)
# ascending=False -> "Bade se chhota" (Seedhi neeche utarna: 10, 9, 8...)


# 6A. Ek column se sort karna (Sabse buzurg pehle):
df_sorted_age = df.sort_values(by='Age', ascending=False)
print("\n--- 6A. Sorted by Age (Descending - Sabse zyada umar pehle) ---")
print(df_sorted_age[['Patient_ID', 'Age', 'Disease']].head(4))


# 6B. Do columns se sort karna:
# Pehle Department A se Z, fir unke andar sabse mehenga patient sabse upar:
df_sorted_multi = df.sort_values(
    by=['Department', 'Treatment_Cost'],
    ascending=[True, False]
)
print("\n--- 6B. Department (A-Z) fir Treatment_Cost (Highest first) ---")
print(df_sorted_multi[['Department', 'Treatment_Cost', 'Disease']].head(6))






# ==============================================================================
# 7. FILTERING WITH CONDITIONS -> "Filter lagao, kaam ka data nikalo"
# ==============================================================================
# 3 GOLDEN RULES (Galti yahin hoti hai):
#  1. Har condition ko BRACKET ( ) me band karo! -> (df['Age'] > 50)
#  2. English ke 'and'/'or' mat likho!
#     Use karo:
#        &  matlab AND (Dono shartein poori honi chahiye)
#        |  matlab OR  (Koi ek bhi shart chalegi)
#        ~  matlab NOT (Yeh nahi hona chahiye)
#  3. Agar multiple options match karne hain, toh .isin([list]) use karo!


# 7A. Ek simple shart (Umar 50 ya zyada):
seniors = df[df['Age'] >= 50]
print(f"\n--- 7A. Filter: Age >= 50 ({len(seniors)} patients mile) ---")
print(seniors[['Patient_ID', 'Age', 'Disease']].head(3))


# 7B. Do shartein ek saath (& se):
# "Cardiology department ka ho AUR kharcha 20,000 se zyada ho"
cardio_high_cost = df[(df['Department'] == 'Cardiology') & (df['Treatment_Cost'] > 20000)]
print("\n--- 7B. Filter: Department == 'Cardiology' AND Treatment_Cost > 20000 ---")
print(cardio_high_cost[['Patient_ID', 'Department', 'Treatment_Cost']])


# 7C. .isin() - "Inme se koi bhi bimari chalegi":
fever_asthma = df[df['Disease'].isin(['Fever', 'Asthma'])]
print("\n--- 7C. Filter using .isin(['Fever', 'Asthma']) ---")
print(fever_asthma[['Patient_ID', 'Disease']].head(4))






# ==============================================================================
# 8. REPLACING VALUES & COLUMN OPERATIONS
# ==============================================================================
# MNEMONIC:
#  to_replace = "Kisko hatana hai"
#  value      = "Uski jagah kisko bithana hai"
#
#  df['Naya_Col'] = df['Purana_Col']  -> "Purane se naya column banao"


# 8A. Single value replace karna:
# 'Yes' ko 'Insured' banao, 'No' ko 'Uninsured' banao:
df['Insurance_Status'] = df['Insurance'].replace(to_replace="Yes", value="Insured")
df['Insurance_Status'] = df['Insurance_Status'].replace(to_replace="No", value="Uninsured")
print("\n--- 8A. Created 'Insurance_Status' via .replace(to_replace=..., value=...) ---")
print(df[['Patient_ID', 'Insurance', 'Insurance_Status']].head(4))


# 8B. List use karke ek saath badalna (Short cut):
# to_replace=['Yes', 'No'], value=[1, 0]
df['Insurance_Code'] = df['Insurance'].replace(
    to_replace=["Yes", "No"],
    value=[1, 0]
)
print("\n--- 8B. List replacement (Yes ko 1, No ko 0) ---")
print(df[['Patient_ID', 'Insurance', 'Insurance_Code']].head(4))


# 8C. Dictionary se badalna (Sabse clean & practical tareeka):
df['Gender_Short'] = df['Gender'].replace({
    "Male": "M",
    "Female": "F"
})
print("\n--- 8C. Dictionary replacement ('Male'->'M', 'Female'->'F') ---")
print(df[['Patient_ID', 'Gender', 'Gender_Short']].head(4))


# 8D. Poore DataFrame me jahan bhi ho wahan replace kar do:
# (Agar column nahi bataya, toh pandas har column me dhoondhta hai):
df_general_replace = df.replace(to_replace="Fever", value="Viral Fever")
print("\n--- 8D. Entire DataFrame replace ('Fever' -> 'Viral Fever') ---")
print(df_general_replace[['Patient_ID', 'Disease']].head(4))


# 8E. Maths karke naya column banana:
# Per day cost = Total Cost / Kitne din ruka
df['Cost_Per_Day'] = (df['Treatment_Cost'] / df['Days_Admitted']).round(2)
print("\n--- 8E. Calculated column: Cost_Per_Day = Treatment_Cost / Days_Admitted ---")
print(df[['Patient_ID', 'Treatment_Cost', 'Days_Admitted', 'Cost_Per_Day']].head(4))


# 8F. Condition ke hisaab se naya column banana via .loc:
# df.loc[ shart , 'Column_Ka_Naam' ] = 'Value'
df.loc[df['Age'] >= 60, 'Age_Category'] = 'Senior'
df.loc[(df['Age'] >= 30) & (df['Age'] < 60), 'Age_Category'] = 'Adult'
df.loc[df['Age'] < 30, 'Age_Category'] = 'Young Adult'
print("\n--- 8F. Conditional category column via .loc ---")
print(df[['Patient_ID', 'Age', 'Age_Category']].head(6))






# ==============================================================================
# 9. MISSING VALUES (NaN / None) HANDLING - "Gayab data ko kaise sambhalein?"
# ==============================================================================
# MNEMONIC & FUNDA:
# Data science me sabse pehla dukh hota hai "Missing Values" (NaN = Not a Number).
# Sambhalne ke 3 hi raaste hote hain:
#   1. Pata lagao:    isna().sum()      ("Kahan kitna data gayab hai?")
#   2. Fenko/Hatao:   dropna()          ("Bhai hatao is row ko, kaam ki nahi hai")
#   3. Bharo:         fillna()          ("Khali jagah bharo - Mean, Median ya Mode se")


# Demo ke liye ek chhota sa copy banate hain jisme thode NaNs daal dete hain:
demo_missing = df[['Patient_ID', 'Age', 'Disease', 'Treatment_Cost', 'Insurance']].head(6).copy()
demo_missing.loc[1, 'Age'] = np.nan
demo_missing.loc[3, 'Disease'] = np.nan
demo_missing.loc[4, 'Treatment_Cost'] = np.nan
demo_missing.loc[5, 'Insurance'] = np.nan

print("\n--- 9. DEMO DATAFRAME WITH MISSING VALUES (NaN) ---")
print(demo_missing)


# ------------------------------------------------------------------------------
# STEP 9A: DETECT KARNA (Check karna kahan kitni kami hai)
# ------------------------------------------------------------------------------
# df.isna().sum() -> Har column me kitne NaNs hain!
print("\n--- 9A. Har Column Me Missing Values Ka Count ---")
print(demo_missing.isna().sum())

print("\nPoore DataFrame me total kitne NaNs hain?:", demo_missing.isna().sum().sum())

# Sirf wahi rows dekhna jahan 'Age' gayab hai:
print("\nRows jahan 'Age' NaN hai:")
print(demo_missing[demo_missing['Age'].isna()])


# ------------------------------------------------------------------------------
# STEP 9B: HATA DENA (dropna) -> "Jo gayab hai, uski row hata do"
# ------------------------------------------------------------------------------
# 1. dropna()              -> Agar kisi row me ek bhi NaN hai, puri row delete!
# 2. dropna(how='all')     -> Sirf tab delete karo jab saare ke saare columns NaN hon.
# 3. dropna(subset=['Col'])-> Sirf tab delete karo jab us specific column me NaN ho.
# 4. dropna(axis=1)        -> Puri column hi uda do jisme NaN hai.

print("\n--- 9B-1. dropna(): Ek bhi NaN mila toh row delete ---")
print(demo_missing.dropna())

print("\n--- 9B-2. dropna(subset=['Age']): Sirf tab hatao agar 'Age' missing ho ---")
print(demo_missing.dropna(subset=['Age']))


# ------------------------------------------------------------------------------
# STEP 9C: KHALI JAGAH BHARNA (fillna) -> "Imputation"
# ------------------------------------------------------------------------------
# Golden Rules:
# * Number column hai aur normal data hai   -> MEAN se bharo
# * Number column me bade outliers hain     -> MEDIAN se bharo (bich ka number)
# * Text / Category column hai              -> MODE se bharo (jo sabse zyada baar aaya)


# Tareeka 1: Constant value daal do ("Not Specified")
fill_constant = demo_missing.copy()
fill_constant['Insurance'] = fill_constant['Insurance'].fillna("Not Specified")
print("\n--- 9C-1. fillna() with Constant ('Not Specified') ---")
print(fill_constant[['Patient_ID', 'Insurance']])


# Tareeka 2: Mean (Average) aur Median se bharna:
fill_stats = demo_missing.copy()
fill_stats['Age'] = fill_stats['Age'].fillna(fill_stats['Age'].mean())
fill_stats['Treatment_Cost'] = fill_stats['Treatment_Cost'].fillna(fill_stats['Treatment_Cost'].median())
print("\n--- 9C-2. fillna() with Mean (Age) & Median (Treatment_Cost) ---")
print(fill_stats[['Patient_ID', 'Age', 'Treatment_Cost']])


# Tareeka 3: Mode (Sabse common value) se text column bharna:
fill_mode = demo_missing.copy()
fill_mode['Disease'] = fill_mode['Disease'].fillna(fill_mode['Disease'].mode()[0])
print("\n--- 9C-3. fillna() with Mode for Categorical ('Disease') ---")
print(fill_mode[['Patient_ID', 'Disease']])


# Tareeka 4: Forward Fill (ffill) & Backward Fill (bfill)
# ffill -> "Pichle bande se copy maro" (Pichli valid value neeche le aao)
# bfill -> "Agle bande se copy maro" (Aage wali valid value upar le aao)
fill_ffill = demo_missing.copy()
fill_ffill['Disease'] = fill_ffill['Disease'].ffill()
print("\n--- 9C-4. ffill(): Forward Fill (Pichle row ki value copy hui) ---")
print(fill_ffill[['Patient_ID', 'Disease']])


# Tareeka 5: Ek Dictionary se har column ko alag alag value se bharna:
fill_dict = demo_missing.copy()
fill_dict = fill_dict.fillna({
    'Age': fill_dict['Age'].mean(),
    'Disease': 'General Checkup',
    'Treatment_Cost': 0,
    'Insurance': 'No'
})
print("\n--- 9C-5. fillna() using Dictionary (Har column ka apna hisaab) ---")
print(fill_dict)


# ------------------------------------------------------------------------------
# STEP 9D: INTERPOLATE() -> "Beech ka hisaab lagao"
# ------------------------------------------------------------------------------
# Agar row 0 par 25 hai aur row 2 par 32 hai, toh beech wali row 1 ka average nikaal lega:
fill_interp = demo_missing.copy()
fill_interp['Age'] = fill_interp['Age'].interpolate(method='linear')
print("\n--- 9D. interpolate() linear for 'Age' ---")
print(fill_interp[['Patient_ID', 'Age']])


# ------------------------------------------------------------------------------
# STEP 9E: CHHUPA HUA KACHRA HATAO ('?', -999, 'NA' ko NaN banao)
# ------------------------------------------------------------------------------
# Asli duniya me log NaN ki jagah '?', '-999', 'NA' likh dete hain.
# Pehle unhe np.nan banao, fir upar wale saare tools kaam karenge:
dirty_data = pd.DataFrame({
    "Score": [90, "?", 85, -999, "NA"],
    "City": ["Delhi", "Mumbai", "Unknown", "Chennai", "Delhi"]
})
print("\n--- 9E. Dirty Placeholders ('?', -999, 'NA') ko NaN Banana ---")
clean_data = dirty_data.replace(to_replace=["?", -999, "NA", "Unknown"], value=np.nan)
print("Before Clean:\n", dirty_data)
print("\nAfter converting to true NaN:\n", clean_data)
print("\nAb dekho missing count:\n", clean_data.isna().sum())






# ==============================================================================
# 10. NUMPY BONUS: np.arange() AUR .reshape()
# ==============================================================================
# MNEMONIC & SPELLING RULE:
# * arange me SINGLE 'r' hota hai -> 'a-range' = "Array Range"
# * Python ke range() jaisa hi hai, par yeh NumPy Array banata hai aur DECIMALS bhi leta hai!
#
# RESHAPE KA GOLDEN RULE:
# * Rows * Columns = Total elements hona chahiye!
# * Magic '-1': "Bhai ek dimension tu khud hisaab laga le, mujhe math nahi karni!"
# ------------------------------------------------------------------------------


# 10A. np.arange() Basics:
arr_1d = np.arange(1, 13)  # 1 se 12 tak ke 12 numbers
print("\n--- 10A. np.arange(1, 13) ---")
print("1D Array:", arr_1d)

# Decimals ke saath arange:
arr_float = np.arange(0, 2, 0.5)  # [0. , 0.5, 1. , 1.5]
print("Decimals wala arange:", arr_float)


# 10B. .reshape() Basics:
# 12 numbers ko 3 rows aur 4 columns ki grid me badalna (3 * 4 = 12):
arr_2d = arr_1d.reshape(3, 4)
print("\n--- 10B. .reshape(3, 4) (3 rows, 4 columns) ---")
print(arr_2d)

# 12 numbers ko 4 rows aur 3 columns me badalna (4 * 3 = 12):
print("\n--- .reshape(4, 3) (4 rows, 3 columns) ---")
print(arr_1d.reshape(4, 3))


# 10C. The Magic '-1' in .reshape():
# Jaise humne poochha tha: np.arange(15, 30).reshape(5, -1)
# 15 se 29 = 15 numbers. 5 rows bol diya, aur column ki jagah -1 laga diya.
# NumPy ne khud hisaab lagaya: 15 / 5 = 3 columns!
print("\n--- 10C. .reshape(2, -1) (NumPy khud nikalega: 12/2 = 6 columns) ---")
print(arr_1d.reshape(2, -1))

demo_user_q = np.arange(15, 30).reshape(5, -1)
print("\n--- np.arange(15, 30).reshape(5, -1) Output ---")
print(demo_user_q)


# 10D. Pandas me iska practical use:
# 1. Fataphat ek dummy DataFrame banana testing ke liye:
test_df = pd.DataFrame(
    np.arange(1, 13).reshape(4, 3),
    columns=['Col_A', 'Col_B', 'Col_C']
)
print("\n--- 10D. Quick DataFrame created using arange + reshape ---")
print(test_df)

# 2. Machine Learning me ek column ko 2D array banana:
# Scikit-Learn models ko 1D column (20,) nahi, 2D matrix (20, 1) chahiye hota hai:
age_2d = df['Age'].values.reshape(-1, 1)
print("\nShape of df['Age'].values (1D):", df['Age'].values.shape)
print("Shape of df['Age'].values.reshape(-1, 1) (2D for ML):", age_2d.shape)