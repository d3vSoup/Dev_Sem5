# ==============================================================================
# TIME SERIES DATA: COMPLETE BEGINNER-FRIENDLY GUIDE & CODE
# ==============================================================================
# What is Time Series Data?
# Time Series data is simply a sequence of data points recorded at successive,
# equally spaced points in time (e.g. hourly temperature, daily stock prices,
# monthly store revenue, yearly website visitors).
#
# WHY IS TIME SERIES SPECIAL?
# 1. Order Matters: You CANNOT randomly shuffle rows! The past influences the future.
# 2. Key Components:
#    - Trend: Long-term general upward or downward direction.
#    - Seasonality: Repeating patterns at regular intervals (e.g., weekend sales surge).
#    - Noise: Unpredictable, random daily fluctuations.
#
# CORE TOOLKIT COVERED IN THIS FILE:
# 1. Parsing dates with pd.to_datetime()
# 2. Setting DatetimeIndex for date slicing (df['2024-03':'2024-06'])
# 3. Extracting date features (.dt.year, .dt.month, .dt.day_name(), etc.)
# 4. Resampling & Frequency conversion (df.resample('M').sum())
# 5. Rolling Windows & Moving Averages (smoothing noise with .rolling())
# 6. Lag features & Shifting (.shift(1), .pct_change(), .diff())
# 7. Complete Time Series Visualization with Matplotlib
# ==============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("==================================================================")
print("1. CREATING A SAMPLE TIME SERIES DATASET")
print("==================================================================")
# Suppose we operate an e-commerce website tracking daily sales for 2023 & 2024.

np.random.seed(42)
# pd.date_range generates a sequence of dates
dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')
n_days = len(dates)

# Simulate realistic sales data:
# Baseline upward trend + weekly seasonality (weekends have +35 sales) + noise
trend = np.linspace(100, 250, n_days)
seasonality = np.where(dates.dayofweek >= 5, 35, 0)
noise = np.random.normal(0, 15, n_days)
sales = np.round(trend + seasonality + noise, 2)

# Raw DataFrame where 'Date' starts as plain string
df_raw = pd.DataFrame({
    'Date_String': dates.strftime('%Y-%m-%d'),
    'Sales': sales,
    'Visitors': np.random.randint(500, 2500, size=n_days)
})

print("Raw DataFrame Preview:")
print(df_raw.head())
print("Data Types before conversion:")
print(df_raw.dtypes)


print("\n==================================================================")
print("2. PARSING DATES (pd.to_datetime) & EXTRACTING DATE FEATURES")
print("==================================================================")
# Convert string to true pandas datetime object
df_raw['Date'] = pd.to_datetime(df_raw['Date_String'])

# Once converted to datetime, you unlock the powerful .dt accessor:
df_raw['Year'] = df_raw['Date'].dt.year
df_raw['Month'] = df_raw['Date'].dt.month
df_raw['Month_Name'] = df_raw['Date'].dt.month_name()
df_raw['Day'] = df_raw['Date'].dt.day
df_raw['Day_Name'] = df_raw['Date'].dt.day_name()
df_raw['Is_Weekend'] = df_raw['Date'].dt.dayofweek >= 5  # 5=Sat, 6=Sun
df_raw['Quarter'] = df_raw['Date'].dt.quarter

print("DataFrame after extracting date components:")
print(df_raw[['Date', 'Year', 'Month_Name', 'Day_Name', 'Is_Weekend', 'Sales']].head(6))


print("\n==================================================================")
print("3. SETTING DATETIMEINDEX & INTUITIVE DATE SLICING")
print("==================================================================")
# When you set Date as the DataFrame Index, Pandas turns into a time machine!
# You can slice and filter dates using plain strings.

df_ts = df_raw.set_index('Date').copy()
# Sort index to ensure chronological ordering
df_ts = df_ts.sort_index()

print("1. Slice by Entire Year (df_ts['2023']):")
print(f"Total rows in 2023: {len(df_ts.loc['2023'])}")

print("\n2. Slice by a Specific Month (df_ts['2024-03']):")
print(df_ts.loc['2024-03', ['Sales', 'Visitors']].head(4))

print("\n3. Slice a Date Range (df_ts['2023-12-25':'2024-01-05']):")
print(df_ts.loc['2023-12-25':'2024-01-05', ['Sales', 'Day_Name']])


print("\n==================================================================")
print("4. RESAMPLING: 'GROUPBY' FOR TIME DATA (df.resample)")
print("==================================================================")
# Resampling converts data from one time frequency to another.
# Downsampling: Higher frequency -> Lower frequency (e.g. Daily to Monthly sum)
# Common Frequency Aliases:
#   'W'  : Weekly
#   'ME' / 'M' : Month End
#   'QE' / 'Q' : Quarter End
#   'YE' / 'Y' : Year End

# Calculate Total Monthly Sales
monthly_sales = df_ts['Sales'].resample('ME').sum()
print("Total Monthly Sales (Last 5 months):")
print(monthly_sales.tail(5).round(2))

# Calculate Average Weekly Sales
weekly_avg = df_ts['Sales'].resample('W').mean()
print("\nAverage Weekly Sales (Last 5 weeks):")
print(weekly_avg.tail(5).round(2))


print("\n==================================================================")
print("5. ROLLING WINDOWS & MOVING AVERAGES (SMOOTHING)")
print("==================================================================")
# Daily data fluctuates wildly. A Moving Average takes the average of the
# previous N days, smoothing out random bumps so you can see real trends.

# 7-day Moving Average (Captures weekly cycles)
df_ts['MA_7'] = df_ts['Sales'].rolling(window=7).mean()

# 30-day Moving Average (Captures monthly trend)
df_ts['MA_30'] = df_ts['Sales'].rolling(window=30).mean()

print("Sales with 7-Day & 30-Day Moving Averages:")
print(df_ts[['Sales', 'MA_7', 'MA_30']].iloc[28:34].round(2))


print("\n==================================================================")
print("6. TIME SHIFTING & LAG FEATURES (FORECASTING ESSENTIALS)")
print("==================================================================")
# .shift(1): Pulls the previous day's value into the current row (Lag 1)
# .diff(): Calculates difference between today and yesterday (today - yesterday)
# .pct_change(): Calculates percentage growth from yesterday

df_ts['Sales_Yesterday'] = df_ts['Sales'].shift(1)
df_ts['Sales_Diff'] = df_ts['Sales'].diff()
df_ts['Daily_Growth_Pct'] = (df_ts['Sales'].pct_change() * 100).round(2)

print("Lag & Growth Features:")
print(df_ts[['Sales', 'Sales_Yesterday', 'Sales_Diff', 'Daily_Growth_Pct']].head(6))


print("\n==================================================================")
print("7. VISUALIZING TIME SERIES DATA")
print("==================================================================")

plt.figure(figsize=(13, 7))

# 1. Plot raw daily sales (with subtle alpha to avoid visual noise)
plt.plot(df_ts.index, df_ts['Sales'], label='Daily Raw Sales', color='lightblue', alpha=0.5, linewidth=1)

# 2. Plot 7-day Moving Average
plt.plot(df_ts.index, df_ts['MA_7'], label='7-Day Moving Avg (Weekly Trend)', color='orange', linewidth=2)

# 3. Plot 30-day Moving Average
plt.plot(df_ts.index, df_ts['MA_30'], label='30-Day Moving Avg (Monthly Trend)', color='crimson', linewidth=2.5)

plt.title('E-Commerce Daily Sales Trend & Moving Averages (2023 - 2024)', fontsize=15, fontweight='bold', pad=15)
plt.xlabel('Date', fontsize=12, fontweight='bold')
plt.ylabel('Sales Volume (USD)', fontsize=12, fontweight='bold')
plt.legend(loc='upper left', frameon=True, shadow=True)
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
print("Displaying Time Series Trend & Moving Averages...")
plt.show()


# Subplot: Monthly Resampled Total Sales Bar Chart
plt.figure(figsize=(12, 5))
monthly_bar_labels = monthly_sales.index.strftime('%b %Y')
plt.bar(monthly_bar_labels, monthly_sales.values, color='teal', edgecolor='black', alpha=0.85)

plt.title('Total Aggregated Monthly Sales (Resampled)', fontsize=14, fontweight='bold', pad=12)
plt.xlabel('Month', fontsize=11, fontweight='bold')
plt.ylabel('Total Sales (USD)', fontsize=11, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle=':', alpha=0.7)

plt.tight_layout()
print("Displaying Monthly Resampled Sales Bar Plot...")
plt.show()

print("\nAll Time Series operations completed successfully!")
