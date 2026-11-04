# ==============================================================================
# DATA VISUALIZATION WITH MATPLOTLIB
# ==============================================================================
# Matplotlib is the fundamental 2D plotting library in Python.
# It enables the creation of static, animated, and interactive visualizations.
#
# Plots covered in this file:
# 1. Bar Plot (Categorical distributions / ODI Cricket Run scoring)
# 2. Scatter Plot (Point distribution, custom sizes, viridis colormap, colorbar & seed)
# 3. Histogram (Continuous frequency distributions / Student scores)
# 4. Pie Chart (Proportions / FIFA World Cup wins by country with explode & shadow)
# 5. Linear / Line Plot (Progression tracking / T20 Cricket run scoring)
# 6. Linear Plot with Custom Line Formatting (Markers, dashed styles, colors, linewidth)
# ==============================================================================

import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------
# 1. BAR PLOT: Runs Scored in an ODI Match by Overs
# ------------------------------------------------------------------------------
# A bar plot represents categorical data with rectangular bars whose heights
# or lengths are proportional to the values they represent.

categories = ['0-10', '10-20', '20-30', '30-40', '40-50']
values = [55, 48, 25, 68, 90]

plt.figure(figsize=(8, 5))
# Create the bar plot
# 'color' specifies the bar fill color
plt.bar(categories, values, color='skyblue', edgecolor='navy', linewidth=1.2)

# Adding labels and titles
plt.xlabel('Overs', fontsize=12, fontweight='bold')
plt.ylabel('Runs', fontsize=12, fontweight='bold')
plt.title('Bar Plot Showing Runs Scored in an ODI Match', fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.7)

print("Displaying 1: Bar Plot...")
plt.show()


# ------------------------------------------------------------------------------
# 2. SCATTER PLOT: Multi-Variable Visualization with Random Seed
# ------------------------------------------------------------------------------
# Scatter plots display values for two numerical variables as points on Cartesian coordinates.
# We can represent additional dimensions using point size (s) and color mapping (c).

# np.random.seed(42):
# Sets the starting point for generating pseudo-random numbers.
# 42 is the seed value.
# Every time you execute the program, NumPy generates the exact same sequence of numbers.
np.random.seed(42)

# Create 50 random data points for X and Y coordinates (scaled to 0-100)
x = np.random.rand(50) * 100
y = np.random.rand(50) * 100

# Generate random sizes and distinct colors for each individual point
sizes = np.random.rand(50) * 500  # Sizes will range up to 500
colors = np.random.rand(50)       # Colors will map to a colormap spectrum

# Configure the plot layout
plt.figure(figsize=(9, 6))

# 's' controls point sizes
# 'c' handles the color values mapped via 'cmap'
# 'alpha' controls transparency (useful for overlapping points)
# 'edgecolors' outlines each circle
scatter = plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.7, edgecolors='black')

# Add chart labels, title, and a color legend bar
plt.title("Demonstration of a Matplotlib Scatter Plot", fontsize=14, fontweight='bold')
plt.xlabel("X-Axis (Variable A)", fontsize=12)
plt.ylabel("Y-Axis (Variable B)", fontsize=12)
plt.colorbar(scatter, label='Color Scale Intensity')  # Displays the color scale legend

# Add a background grid for easier reading
plt.grid(True, linestyle='--', alpha=0.5)

print("Displaying 2: Scatter Plot...")
plt.show()


# ------------------------------------------------------------------------------
# 3. HISTOGRAM: Distribution of Student Scores
# ------------------------------------------------------------------------------
# A histogram displays the frequency distribution of continuous numerical data.
# Data is grouped into contiguous ranges called 'bins'.

np.random.seed(42)
# Generate 100 random student scores following a normal distribution
# loc = mean (70), scale = standard deviation (15)
student_scores = np.random.normal(loc=70, scale=15, size=100)

plt.figure(figsize=(8, 5))
# Create a histogram plot
# bins=20 splits data into 20 equal-width bins
plt.hist(student_scores, bins=20, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Student Scores', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Student Scores', fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle=':', alpha=0.6)

print("Displaying 3: Histogram...")
plt.show()


# ------------------------------------------------------------------------------
# 4. PIE CHART: FIFA World Cup Wins by Country
# ------------------------------------------------------------------------------
# A pie chart illustrates numerical proportions as circular slices.
# The arc length of each slice is proportional to the quantity it represents.

countries = ['Brazil', 'Germany', 'Italy', 'Argentina', 'Uruguay', 'France', 'England', 'Spain']
wins = [5, 4, 4, 3, 2, 2, 1, 1]

# Distinct colors for each country slice
colors = ['yellow', 'magenta', 'green', 'blue', 'lightblue', 'gold', 'red', 'cyan']

plt.figure(figsize=(8, 8))
# autopct='%1.1f%%': Formats percentage to 1 decimal place
# startangle=90: Rotates start angle to 12 o'clock
# explode: Offsets slices away from center for visual emphasis
# shadow=True: Adds a drop-shadow depth effect
plt.pie(
    wins,
    labels=countries,
    autopct='%1.1f%%',
    colors=colors,
    startangle=90,
    explode=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
    shadow=True
)

plt.title('FIFA World Cup Wins by Country', fontsize=14, fontweight='bold')

# plt.axis('equal') ensures the pie chart is drawn as a perfect circle (not an ellipse)
plt.axis('equal')

print("Displaying 4: Pie Chart...")
plt.show()


# ------------------------------------------------------------------------------
# 5. LINEAR / LINE PLOT: T20 Cricket Match Run Rate Progression
# ------------------------------------------------------------------------------
# A line plot connects sequential data points with straight line segments,
# showing trends over an ordered sequence (like time or overs).

overs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
runs_scored = [0, 7, 12, 20, 39, 49, 61, 83, 86, 97, 113, 116, 123, 137, 145, 163, 172, 192, 198, 198, 203]

plt.figure(figsize=(8, 5))
# Create standard linear plot
plt.plot(overs, runs_scored)

plt.xlabel('Overs', fontsize=12)
plt.ylabel('Runs scored', fontsize=12)
plt.title('Run scoring in a T20 Cricket Match (Basic Line Plot)', fontsize=13, fontweight='bold')
plt.grid(True)

print("Displaying 5: Basic Line Plot...")
plt.show()


# ------------------------------------------------------------------------------
# 6. LINEAR PLOT WITH ADVANCED LINE FORMATTING
# ------------------------------------------------------------------------------
# Matplotlib allows deep customization of line formatting:
# - marker: Symbol at each data point ('X', 'o', 's', '^', etc.)
# - linestyle: Style of connecting line ('dashed', 'dotted', 'solid', '-.')
# - color: Color of the line
# - linewidth: Width / thickness of the line
# - markerfacecolor: Fill color inside the marker
# - markersize: Diameter of the marker
# - Custom label colors (e.g. plt.xlabel(..., color='green'))

plt.figure(figsize=(9, 5))
plt.plot(
    overs,
    runs_scored,
    marker='X',
    linestyle='dashed',
    color='red',
    linewidth=2,
    markerfacecolor='blue',
    markersize=8
)

plt.xlabel('Overs', color='green', fontsize=12, fontweight='bold')
plt.ylabel('Runs scored', fontsize=12, fontweight='bold')
plt.title('Run scoring in a T20 Cricket Match (Custom Line Formatting)', fontsize=13, fontweight='bold')
plt.grid(True, linestyle=':', alpha=0.6)

print("Displaying 6: Line Plot with Custom Line Formatting...")
plt.show()



# so basically if i want  to plot a  graph or a picture then i have to import matplotlib 
# and if i want to plot a graph  or a picture using numpy then i have to import numpy 




