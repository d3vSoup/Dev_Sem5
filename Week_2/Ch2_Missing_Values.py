''' NAN


In pandas, missing values appear as NaN (Not a Number), representing absent or undefined values. 

The primary causes are:   
            External retrieval issues: Extracting incomplete records from outside data sources.   
            Join mismatches: Merging datasets where keys in one table do not exist in the other.   
            Data collection errors: Hardware sensor failures, dropped packets, or manual omissions.   
            Dimensional structural shifts: Reshaping or unstacking operations that introduce unpopulated grid intersections.   
            Reindexing: Aligning an existing series/table against a new index set.






'''


# ==============================================================================
# MISSING VALUES IN PANDAS (FRUIT STORE INVENTORY - DESI EDITION)
# ==============================================================================
# Is file me hum:
# 1. 6 Fruits (Rows) x 5 Stores (Columns) ka table banayenge using np.arange().reshape()
# 2. .loc aur np.nan se alag alag jagah missing values daalenge
# 3. .loc aur np.arange se row update karenge
# 4. Missing values ko dhoondna, drop karna, aur fill karna seekhenge!
# ==============================================================================

import pandas as pd
import numpy as np

# Deprecation warning silent rakhne ke liye:
pd.set_option('future.no_silent_downcasting', True)






# ==============================================================================
# 1. TABLE BANANA: np.arange() AUR .reshape() SE
# ==============================================================================
# Humaare pass:
#  - 6 Fruits (Rows): Apple, Orange, Watermelon, Banana, Mango, Grapes
#  - 5 Stores (Columns): Store_1, Store_2, Store_3, Store_4, Store_5
#
# Math: 6 rows * 5 columns = 30 numbers chahiye!
# np.arange(10, 40) -> 10 se 39 tak ke 30 numbers
# .reshape(6, 5)    -> 6 rows aur 5 columns ki 2D grid

fruits = ['Apple', 'Orange', 'Watermelon', 'Banana', 'Mango', 'Grapes']
stores = ['Store_1', 'Store_2', 'Store_3', 'Store_4', 'Store_5']

#how is it making the fruits and stores to make a dataframe ?
# ans - the fruits are making index (rows) and the stores are making columns and the numbers are the values in the cells
# Data grid banana:
fruit_data = np.arange(10, 40).reshape(6, 5)

# DataFrame banana (Index me fruits, Columns me stores):
df = pd.DataFrame(fruit_data, index=fruits, columns=stores)

print("--- 1. ORIGINAL FRUIT STORE TABLE (No Missing Data Yet) ---")
print(df)






# ==============================================================================
# 2. MISSING VALUES (np.nan) AUR np.arange SE ROWS UPDATE KARNA
# ==============================================================================
# MNEMONIC:
# df.loc[ 'Fruit_Naam' , 'Store_Naam' ] = np.nan
# "Apple ka Store_2 me stock khatam ho gaya (NaN ban gaya)"

# 2A. Single Cell me NaN daalna (.loc se):
df.loc['Apple', 'Store_2'] = np.nan


# 2B. Multiple Stores me ek saath NaN daalna:
# Watermelon ka Store_1 aur Store_4 dono me data gayab:
df.loc['Watermelon', ['Store_1', 'Store_4']] = np.nan


# 2C. .iloc (Position) se kisi cell ko NaN banana:
# Mango (Row 4) ke Store_3 (Col 2) me NaN:
df.iloc[4, 2] = np.nan


# 2D. .loc + np.arange se poori row update karna:
# "Banana ka naya stock aaya (5 stores ke liye 5 numbers: 100, 101, 102, 103, 104)"
df.loc['Banana'] = np.arange(100, 105)

# Aur Banana ka Store_5 me stock galti se missing hai:
df.loc['Banana', 'Store_5'] = np.nan


# 2E. Grapes ka Store_3 me stock missing:
df.loc['Grapes', 'Store_3'] = np.nan


print("\n--- 2. TABLE WITH MISSING VALUES (np.nan injected) ---")
print(df)




# difference between isna() and isnull() ?
# ans - There is absolutely no difference between .isna() and .isnull(). Both functions are exactly identical and do the same thing in Pandas.

# ==============================================================================
# 3. MISSING VALUES DHOONDNA: isna(), isnull(), AUR notnull()
# ==============================================================================
# DESI FUNDA & MNEMONIC:
#  * .isna()   & .isnull()  -> "Kya data gayab hai?" (True = NaN, False = Data hai)
#  * .notna()  & .notnull() -> "Kya data theek-thaak hai?" (True = Data hai, False = NaN)
#
# ------------------------------------------------------------------------------
# WHY .isnull().sum() WORKS? (INTERVIEW & EXAM FAVOURITE QUESTION!):
#  * Python me Boolean values numbers ki tarah behave karti hain:
#        True  = 1
#        False = 0
#  * Jab hum df.isnull() karte hain, table me True aur False bhar jaata hai.
#  * Fir jab hum .sum() lagate hain, Python saare 1s (True) ko jod deta hai!
#    Example: [False, True, True] -> [0, 1, 1] -> Sum = 2 missing values!
#
# WHY TWO .sum().sum() FOR FULL DATAFRAME?
#  * 1st .sum(): df.isnull().sum()
#    -> Yeh har column ka sum nikalta hai (gives a Series of 5 numbers).
#  * 2nd .sum(): df.isnull().sum().sum()
#    -> Yeh un 5 column sums ko aapas me jod deta hai (Grand Total of Full DF)!
#  * (Bonus): df.isnull().values.sum() bhi wahi karta hai.
# ------------------------------------------------------------------------------


# 3A. isna(): Store-wise Missing Count (Column-wise):
print("\n--- 3A. Store-wise Missing Count using .isna().sum() ---")
print(df.isna().sum())


# 3B. isnull(): Fruit-wise Missing Count (Row-wise: axis=1):
# TRICK: axis=1 lagane se row-wise (fruit-wise) ginti aati hai
print("\n--- 3B. Fruit-wise Missing Count using .isnull().sum(axis=1) ---")
print(df.isnull().sum(axis=1))


# 3C. notnull(): Valid Data dekhna (isnull ka bilkul ulta):
# True = Available stock (1), False = Missing stock (0)
print("\n--- 3C. df.notnull() Grid (True = Stock Available) ---")
print(df.notnull())

# notnull() se filter karna: Sirf wo fruits dikhao jinka Store_1 me valid stock hai:
print("\nFruits with valid stock in Store_1 (using .notnull()):")
print(df[df['Store_1'].notnull()][['Store_1']])


# 3D. Full DataFrame ka Grand Total Missing Count:
print("\n--- 3D. Grand Total of Missing Values in Full DataFrame ---")
print("Pehla .sum() (Har column ka): \n", df.isnull().sum())
print("\nDoosra .sum() (.isnull().sum().sum()) -> Grand Total:", df.isnull().sum().sum()) 
#why two sum ??
# ans - First .sum() gives count of null values in each column. 
# Second .sum() gives the sum of all the counts of null values in each column.
print("Alternative trick (df.isnull().values.sum()):", df.isnull().values.sum())


# 3E. Sirf wahi fruits dikhao jisme kahin na kahin NaN hai:
print("\n--- 3E. Missing stock wale fruits (using .isnull().any(axis=1)) ---")
print(df[df.isnull().any(axis=1)])





# ==============================================================================
# 4. DROPPING MISSING VALUES: dropna() KA COMPLETE MASTER GUIDE
# ==============================================================================
# dropna() ke 5 mukhya hathiyar (Parameters):
#  1. axis    = 0 (Rows hatao - Default)  YA  1 (Columns hatao)
#  2. how     = 'any' (Ek bhi NaN mila toh uda do - Default)  YA  'all' (Saare NaN hone par hi uda do)
#  3. thresh  = N (Kam se kam N valid / non-null values honi chahiye, warna uda do)
#  4. subset  = ['Col1', 'Col2'] (Sirf in chune hue columns me NaN check karo)
#  5. inplace = False (Naya table do - Default)  YA  True (Asli table ko hi badal do)
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 4A. PARAMETER 1: axis (0 = Rows vs 1 = Columns)
# ------------------------------------------------------------------------------
# axis=0 (Default): "Jis Fruit (Row) me NaN hai, us fruit ko hata do"
print("\n--- 4A-1. dropna(axis=0): Default Row-wise Drop ---")
print("Sirf bina kisi NaN wale fruits bachenge (Sirf Orange bacha):")
print(df.dropna(axis=0))


# axis=1: "Jis Store (Column) me NaN hai, us poore store ko hata do"
print("\n--- 4A-2. dropna(axis=1): Column-wise Drop ---")
print("Agar har store me koi na koi fruit missing hai toh empty aayega:")
print(df.dropna(axis=1))




# ------------------------------------------------------------------------------
# 4B. PARAMETER 2: how ('any' vs 'all')
# ------------------------------------------------------------------------------
# MNEMONIC:
#  * how='any' (Default): "Kahin bhi thoda sa bhi daagh (NaN) laga, toh uda do!"
#  * how='all':           "Jab poori row hi khali (sab ke sab NaN) ho, TAB uda do!"

# Dekhne ke liye hum ek dummy fruit 'Pineapple' banate hain jo saare stores me NaN hai:
df_how_demo = df.copy()
df_how_demo.loc['Pineapple'] = np.nan

print("\n--- 4B. Demo Table with a completely empty 'Pineapple' row ---")
print(df_how_demo)

# how='all' -> Sirf Pineapple hatega kyunki sirf Pineapple ke saare 5 stores NaN hain!
print("\n--- dropna(how='all'): Sirf poori tarah khali rows hatengi ---")
print(df_how_demo.dropna(how='all'))

# how='any' -> Har wo fruit hatega jisme 1 bhi NaN hai (Sirf Orange bachega):
print("\n--- dropna(how='any'): Ek bhi NaN hua toh uda dega ---")
print(df_how_demo.dropna(how='any'))




# ------------------------------------------------------------------------------
# 4C. PARAMETER 3: thresh=N (Threshold - "Minimum attendance kitni honi chahiye?")
# ------------------------------------------------------------------------------
# DESI RULE:
# thresh = "Kam se kam itne VALID (NON-NULL) stores me stock hona chahiye!"
# Yaad rakho: thresh NaN ko nahi ginta, VALID VALUES ko ginta hai!
#
# Humaare table me:
#  - Orange     -> 5 valid stores (0 NaN)
#  - Apple      -> 4 valid stores (1 NaN)
#  - Banana     -> 4 valid stores (1 NaN)
#  - Mango      -> 4 valid stores (1 NaN)
#  - Grapes     -> 4 valid stores (1 NaN)
#  - Watermelon -> 3 valid stores (2 NaNs: Store_1 and Store_4)

# Example 1: thresh=4 ("Kam se kam 4 stores me maal hona chahiye")
# -> Watermelon ke paas sirf 3 stores hain, toh Watermelon udd jayega!
print("\n--- 4C-1. dropna(thresh=4): Kam se kam 4 valid values chahiye ---")
print(df.dropna(thresh=4))

# Example 2: thresh=5 ("Saare 5 stores me maal hona chahiye")
# -> Sirf Orange bachega!
print("\n--- 4C-2. dropna(thresh=5): Poore 5 valid values chahiye ---")
print(df.dropna(thresh=5))




# ------------------------------------------------------------------------------
# 4D. PARAMETER 4: subset=['Col1', 'Col2'] -> "Chuninda columns me check karo"
# ------------------------------------------------------------------------------
# MNEMONIC:
# "Bhai baaki stores me jo marzi ho, mujhe sirf Store_1 se matlab hai!"

# Example 1: Check ONLY in 'Store_1'
# -> Watermelon ka Store_1 missing hai, toh sirf Watermelon hatega!
print("\n--- 4D-1. dropna(subset=['Store_1']): Sirf Store_1 ke NaNs dekho ---")
print(df.dropna(subset=['Store_1']))

# Example 2: Check in multiple stores: ['Store_1', 'Store_3']
# -> Store_1 me Watermelon gayab hai, Store_3 me Mango aur Grapes gayab hain.
print("\n--- 4D-2. dropna(subset=['Store_1', 'Store_3']): Store_1 ya Store_3 me missing walo ko hatao ---")
print(df.dropna(subset=['Store_1', 'Store_3']))




# ------------------------------------------------------------------------------
# 4E. PARAMETERS KA COMBINATION: subset + how
# ------------------------------------------------------------------------------
# "Store_1 AUR Store_4 DONO me NaN hona chahiye tabhi hatao"
# -> Watermelon ke Store_1 aur Store_4 DONO NaN hain!
print("\n--- 4E. Combination: subset=['Store_1', 'Store_4'], how='all' ---")
print(df.dropna(subset=['Store_1', 'Store_4'], how='all'))




# ------------------------------------------------------------------------------
# 4F. PARAMETER 5: inplace (False vs True)
# ------------------------------------------------------------------------------
# DESI FUNDA:
#  * inplace=False (Default): "Asli register ko haath mat lagao! Naya xerox copy do."
#  * inplace=True:           "Asli register me se hi panna faad do! (Permanent Change)."
#
# PRO-TIP: inplace=True kuch return nahi karta (None return karta hai).

df_test_inplace = df.copy()

print("\n--- 4F. inplace Demonstration ---")
print("Inplace se pehle rows count:", len(df_test_inplace))

# Asli copy ko permanently badal diya:
df_test_inplace.dropna(subset=['Store_1'], inplace=True)

print("Inplace=True ke baad asli table badal gaya (Watermelon udd gaya):")
print(df_test_inplace)






# ==============================================================================
# 5. MISSING VALUES BHARNA: fillna() -> "Khali dabba bharo"
# ==============================================================================

# Tareeka 5A: Zero (0) se bharo -> "Stock khatam matlab 0"
df_zero = df.fillna(0)
print("\n--- 5A. fillna(0) - Out of stock ko 0 likho ---")
print(df_zero)


# Tareeka 5B: Store ke Average (Mean) se bharo:
# Har store ke bache hue fruits ka average nikal ke missing cell me daalo
df_mean = df.fillna(df.mean().round(1))
print("\n--- 5B. fillna(df.mean()) - Store ke average stock se bharo ---")
print(df_mean)


# Tareeka 5C: Forward Fill (ffill) -> "Pichle store se copy maro"
# axis=1 ka matlab horizontal (Store 1 se Store 2 me copy)
df_ffill = df.ffill(axis=1)
print("\n--- 5C. ffill(axis=1) - Pichle store ki value aage copy karo ---")
print(df_ffill)


# Tareeka 5D: Backward Fill (bfill) -> "Agle store se copy maro"
df_bfill = df.bfill(axis=1)
print("\n--- 5D. bfill(axis=1) - Agle store ki value peeche copy karo ---")
print(df_bfill)


# Tareeka 5E: Har Store ke liye alag value (Dictionary Mapping):
df_custom = df.fillna({
    'Store_1': 99,
    'Store_2': 50,
    'Store_3': 0,
    'Store_4': 25,
    'Store_5': 10
})
print("\n--- 5E. fillna(dict) - Har store ka apna custom fill number ---")
print(df_custom)









# ==============================================================================
# 6. WHAT DOES .count() DO? & ITS VARIATIONS -> "Kitne log haazir hain?"
# ==============================================================================
# DESI FUNDA & MNEMONIC:
# * .count() school ke attendance register ki tarah hai!
# * Yeh sirf aur sirf PRESENT (NON-NULL / NON-NA) values ko ginta hai.
# * NaN ko yeh BILKUL IGNORE kar deta hai (Chhuti wale ko nahi ginta).
#
# GOLDEN FORMULA TO REMEMBER:
#   .count()  +  .isna().sum()  =  Total Rows (len(df))
#   (Haazir)  +  (Gayab)        =  Total Bachhe
#
# DIFFERENCE: .count() vs len() vs .size
#   - df.count(): Sirf valid / non-null values ginta hai (NaN ignored).
#   - len(df):    Total rows ginta hai (Chahe row me NaN ho ya na ho).
#   - df.size:    Total cells ginta hai (Rows * Columns, including NaNs).
# ------------------------------------------------------------------------------


# 6A. Variation 1: Column-wise count (Default: axis=0)
# "Har Store me kitne valid fruits available hain?"
print("\n--- 6A. Column-wise count (df.count()): Valid fruits per Store ---")
print(df.count())


# 6B. Variation 2: Row-wise count (axis=1)
# "Har Fruit kitne stores me actually available hai?"
print("\n--- 6B. Row-wise count (df.count(axis=1)): Valid stores per Fruit ---")
print(df.count(axis=1))


# 6C. Variation 3: Single Column ka count
print("\n--- 6C. Single Column count: df['Store_1'].count() ---")
print("Valid fruits in Store_1:", df['Store_1'].count())
print("Total rows in Store_1:", len(df['Store_1']))


# 6D. Variation 4: Grand Total of Valid Cells across Full DataFrame
# "Poori dukan me kitne cells me actual stock ka data hai?"
print("\n--- 6D. Grand Total of Valid Cells (df.count().sum()) ---")
print("Total Valid Cells (df.count().sum()):", df.count().sum())
print("Total Cells in Table (df.size):", df.size)
print("Total Missing Cells (df.isnull().sum().sum()):", df.isnull().sum().sum())
print("Formula check (Valid + Missing == Total):", df.count().sum() + df.isnull().sum().sum() == df.size)


# 6E. Variation 5: .value_counts() vs .count() (Interviews ka Favourite)
#  * .count() sirf ek number deta hai (Kitne non-null hain).
#  * .value_counts() batata hai kaunsa item kitni baar aaya (Frequency).
#  * TRICK: value_counts(dropna=False) lagane se NaN ko bhi ginta hai!
sample_series = pd.Series(['Apple', 'Apple', 'Banana', np.nan, 'Apple', np.nan])
print("\n--- 6E. .count() vs .value_counts() on Series ---")
print("Series.count() (NaN ignored):", sample_series.count())  # 4
print("\nSeries.value_counts(dropna=False) (Shows count of NaNs too!):")
print(sample_series.value_counts(dropna=False))

