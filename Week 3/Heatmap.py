# ==============================================================================
# SEABORN HEATMAPS: COMPLETE GUIDE, WHAT TO DO & HOW TO USE
# ==============================================================================
# A Heatmap is a 2D graphical representation where individual matrix values
# are represented as colors. It is the gold standard for visualizing:
#   1. Feature Correlations (Are two features positively or negatively related?)
#   2. Pivot Tables & Cross-Tabs (e.g. Monthly sales across multiple years)
#   3. Confusion Matrices & Frequency Grids
#
# ==============================================================================
# GOLDEN RULE: WHAT TO DO BEFORE CALLING sns.heatmap()
# ==============================================================================
# You CANNOT just pass a regular raw tabular DataFrame directly into a heatmap!
# A heatmap requires a 2D rectangular MATRIX (rows and columns must form a grid).
#
# To prepare your data, you MUST do one of these 3 things first:
#   Option A: Calculate correlation matrix -> df.corr()
#   Option B: Pivot your table into a 2D grid -> df.pivot() or df.pivot_table()
#   Option C: Create a frequency cross-tabulation -> pd.crosstab()
# ==============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("==================================================================")
print("1. CORRELATION HEATMAP (df.corr())")
print("==================================================================")
# Use Case: Find linear relationships between numeric columns.
# Values range from -1.0 (perfect negative) to +1.0 (perfect positive).

# Sample Dataset: Student Study & Exam Performance
np.random.seed(42)
n_students = 100
study_hours = np.random.uniform(2, 10, n_students)
attendance_pct = np.clip(study_hours * 8 + np.random.normal(20, 5, n_students), 40, 100)
sleep_hours = np.random.uniform(5, 9, n_students)
screen_time = 14 - sleep_hours - (study_hours * 0.7) + np.random.normal(0, 1, n_students)
exam_score = np.clip(study_hours * 7 + attendance_pct * 0.3 - screen_time * 1.5 + np.random.normal(10, 4, n_students), 0, 100)

student_df = pd.DataFrame({
    'Study_Hours': study_hours,
    'Attendance_Pct': attendance_pct,
    'Sleep_Hours': sleep_hours,
    'Screen_Time': screen_time,
    'Exam_Score': exam_score
})

print("Dataset Preview:")
print(student_df.head(4).round(2))

# STEP 1: Compute Correlation Matrix
corr_matrix = student_df.corr()
print("\nCorrelation Matrix (2D grid ready for heatmap):")
print(corr_matrix.round(2))

# STEP 2: Plot Heatmap
plt.figure(figsize=(8, 6))

# KEY PARAMETERS EXPLAINED:
# - data: The 2D matrix (corr_matrix)
# - annot=True: Prints the actual numeric value inside each cell
# - fmt='.2f': Formats cell text to 2 decimal places
# - cmap='coolwarm': Diverging colormap (Red = positive correlation, Blue = negative)
# - vmin=-1, vmax=1: Anchors color scale strictly between -1 and +1
# - linewidths=1.5: Adds white grid boundaries separating each cell
# - linecolor='white': Color of the dividing borders
# - cbar=True: Shows the color scale legend on the right

sns.heatmap(
    corr_matrix,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    vmin=-1,
    vmax=1,
    linewidths=1.5,
    linecolor='white',
    cbar=True
)

plt.title('Correlation Heatmap: Student Performance Factors', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
print("Displaying 1: Basic Correlation Heatmap...")
plt.show()


print("\n==================================================================")
print("2. ADVANCED CORRELATION HEATMAP (MASKING UPPER TRIANGLE)")
print("==================================================================")
# Why mask? A correlation matrix is mirror-symmetric across the diagonal.
# The diagonal is always 1.0 (a variable correlated with itself).
# Showing both top and bottom halves is redundant. Hiding the top half
# makes your charts look professional and clean.

# Create a boolean mask of the upper triangle:
# np.triu() returns the upper triangle of any matrix
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    mask=mask,               # Hides upper triangle cells where mask is True
    annot=True,
    fmt='.2f',
    cmap='vlag',             # Another great diverging palette (Blue/White/Red)
    vmin=-1,
    vmax=1,
    center=0,                # Forces 0.0 to be the neutral middle color (white)
    linewidths=2,
    linecolor='white',
    square=True              # Forces each cell to be a perfect square
)

plt.title('Professional Upper-Masked Correlation Heatmap', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
print("Displaying 2: Masked Correlation Heatmap...")
plt.show()


print("\n==================================================================")
print("3. PIVOT TABLE HEATMAP: Monthly Product Sales over Years")
print("==================================================================")
# Use Case: You have two categorical columns (e.g. Month, Year) and one
# numerical metric (e.g. Sales).
# You use df.pivot() or df.pivot_table() to convert it into a 2D matrix.

# Generating simulated monthly sales over 4 years
years = [2021, 2022, 2023, 2024]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

data_records = []
for y in years:
    base = 100 + (y - 2021) * 25
    for m_idx, m in enumerate(months):
        # Seasonality: higher sales in festive months (Nov, Dec), mid-year dip
        seasonal_boost = 50 if m in ['Nov', 'Dec'] else (20 if m in ['Oct', 'Jan'] else 0)
        sales = int(base + seasonal_boost + np.random.normal(10, 5))
        data_records.append({'Year': y, 'Month': m, 'Sales': sales})

sales_df = pd.DataFrame(data_records)

# STEP 1: Pivot into a 2D grid
# rows = Months, columns = Years, values = Sales
sales_pivot = sales_df.pivot(index='Month', columns='Year', values='Sales')

# Preserve calendar month ordering
sales_pivot = sales_pivot.reindex(months)

print("Pivoted Sales Grid:")
print(sales_pivot)

# STEP 2: Plot Heatmap
plt.figure(figsize=(9, 7))

# For sales/counts, a sequential colormap (YlGnBu, Blues, viridis) is best
sns.heatmap(
    sales_pivot,
    annot=True,
    fmt='d',             # 'd' for whole integer numbers
    cmap='YlGnBu',       # Yellow-Green-Blue sequential gradient
    linewidths=1,
    linecolor='gray',
    cbar_kws={'label': 'Units Sold (in Thousands)'}
)

plt.title('Monthly Store Sales Heatmap (2021 - 2024)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Month', fontsize=12, fontweight='bold')
plt.tight_layout()
print("Displaying 3: Sales Pivot Table Heatmap...")
plt.show()


print("\n==================================================================")
print("4. CROSS-TABULATION HEATMAP (pd.crosstab())")
print("==================================================================")
# Use Case: Count how often two categories co-occur.
# Example: Student Grade Distribution vs Preferred Study Method

study_method = np.random.choice(['Self-Study', 'Group Discussion', 'Online Videos', 'Tutor Coaching'], size=150, p=[0.35, 0.25, 0.25, 0.15])
grades = np.random.choice(['A', 'B', 'C', 'D'], size=150, p=[0.30, 0.40, 0.20, 0.10])

eval_df = pd.DataFrame({'Study_Method': study_method, 'Grade': grades})

# STEP 1: Compute cross-tabulation frequency table
ct = pd.crosstab(eval_df['Study_Method'], eval_df['Grade'])
print("Cross-Tabulation Table:")
print(ct)

# STEP 2: Plot Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(
    ct,
    annot=True,
    fmt='d',
    cmap='Purples',
    linewidths=1.2,
    cbar_kws={'label': 'Student Count'}
)

plt.title('Cross-Tabulation: Study Method vs Grade Obtained', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Grade', fontsize=11, fontweight='bold')
plt.ylabel('Study Method', fontsize=11, fontweight='bold')
plt.tight_layout()
print("Displaying 4: Cross-Tabulation Heatmap...")
plt.show()


# ==============================================================================
# QUICK REFERENCE CHEAT-SHEET: COMMON HEATMAP COLORMAPS
# ==============================================================================
# 1. Diverging (Has a meaningful center like 0 or neutral point):
#    - 'coolwarm' : Blue (negative) -> White (zero) -> Red (positive)
#    - 'vlag'     : Dark Blue -> Light -> Dark Red
#    - 'Spectral' : Multi-color gradient
#
# 2. Sequential (For counts, sales, frequencies, magnitudes):
#    - 'YlGnBu'   : Yellow -> Green -> Blue (high readability)
#    - 'Blues'    : Light blue to dark navy
#    - 'viridis'  : Purple -> Teal -> Yellow (perceptually uniform)
#    - 'rocket'   : Dark to bright neon
# ==============================================================================

