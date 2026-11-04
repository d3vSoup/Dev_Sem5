# ==============================================================================
# SEABORN PLOT CUSTOMIZATION WITH AESTHETIC FUNCTIONS
# ==============================================================================
# Seaborn is a Python data visualization library based on Matplotlib.
# It provides a high-level interface for drawing attractive and informative
# statistical graphics.
#
# A central strength of Seaborn is its "Aesthetic Functions" that manage:
# 1. Figure Styles (Themes & Grids): sns.set_style()
# 2. Plot Scaling / Contexts: sns.set_context()
# 3. Overall Theme & Parameters: sns.set() / sns.set_theme()
# 4. Spines Removal: sns.despine()
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------------------------
# THE sinplot() DEMONSTRATION FUNCTION
# ------------------------------------------------------------------------------
# Generates and plots multiple sine waves with progressive phase shifts and
# varying amplitudes to demonstrate how aesthetic changes apply across lines.

def sinplot(n=10):
    """
    Plots n sine waves across the interval [0, 14] with staggered phase
    offsets and amplitude factors.
    """
    x = np.linspace(0, 14, 100)
    for i in range(1, n + 1):
        plt.plot(x, np.sin(x + i * 0.5) * (n + 2 - i))


# ------------------------------------------------------------------------------
# 1. DEFAULT SEABORN AESTHETICS & CONTEXT SCALING
# ------------------------------------------------------------------------------
# From Colab:
# sns.set() sets default seaborn styling.
# sns.set_context() configures scale of elements:
#   - Contexts available:
#       * 'paper'    : smallest, suited for academic documents and print
#       * 'notebook' : default, ideal for screen viewing and jupyter notebooks
#       * 'talk'     : enlarged labels, suited for presentation slides
#       * 'poster'   : largest scaling, designed for large exhibition posters
#   - font_scale     : multiplier for all font labels (1.5 = 150% text size)
#   - rc             : dict of matplotlib rcParams (e.g. lines.linewidth = 2.5)

plt.figure(figsize=(10, 6))

# Apply global seaborn aesthetic theme
sns.set()

# Apply context scaling with font_scale and custom line width
sns.set_context(
    "notebook",
    font_scale=1.5,
    rc={"lines.linewidth": 2.5}
)

# Plot curves using the custom aesthetic configuration
sinplot()

plt.title('Seaborn plots with Aesthetic functions', fontsize=16, fontweight='bold')
print("Displaying 1: Seaborn plot with Aesthetic Functions & Scaling...")
plt.show()


# ------------------------------------------------------------------------------
# 2. EXPLORING SEABORN THEMES & STYLES (sns.set_style)
# ------------------------------------------------------------------------------
# Seaborn provides 5 built-in style presets:
# - 'darkgrid'  : default, dark gray background with white grid lines
# - 'whitegrid' : clean white background with subtle gray grid lines
# - 'dark'      : dark background without grid lines
# - 'white'     : clean white background without grid lines
# - 'ticks'     : white background with tick marks on the axes

styles = ['whitegrid', 'darkgrid', 'ticks', 'white']

plt.figure(figsize=(14, 8))
for idx, style in enumerate(styles, 1):
    plt.subplot(2, 2, idx)
    sns.set_style(style)
    sns.set_context("notebook", font_scale=1.1, rc={"lines.linewidth": 1.8})
    sinplot(n=5)
    plt.title(f"Style: '{style}'", fontsize=12, fontweight='bold')
    if style == 'ticks':
        # sns.despine() removes top and right axis borders for cleaner look
        sns.despine()

plt.tight_layout()
print("Displaying 2: Comparison of 4 Seaborn Aesthetic Styles...")
plt.show()


# ------------------------------------------------------------------------------
# 3. CONTEXT COMPARISON (paper vs talk vs poster)
# ------------------------------------------------------------------------------
# Comparing how set_context changes label and line scales for different targets:
contexts = ['paper', 'talk', 'poster']

for ctx in contexts:
    plt.figure(figsize=(8, 4))
    sns.set_theme(style="whitegrid")  # modern alias for sns.set()
    sns.set_context(ctx)
    sinplot(n=4)
    plt.title(f"Seaborn Context: '{ctx}'", fontweight='bold')
    sns.despine()
    print(f"Displaying Context: {ctx}...")
    plt.show()

