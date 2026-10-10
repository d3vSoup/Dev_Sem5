import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set a beautiful theme for our graphs
sns.set_theme(style="whitegrid", palette="husl")

# Path to the iris.csv file in your Downloads folder
file_path = '/Users/rik_mac/Downloads/iris.csv'

# Read the CSV file into a DataFrame
iris_df = pd.read_csv(file_path)

# Drop the 'Id' column because it's just a row number and we don't want to graph it
if 'Id' in iris_df.columns:
    iris_df.drop('Id', axis=1, inplace=True)

print("Here is the Iris dataset:")
print(iris_df.head())
#head and tail of iris and head ( n ) meaning 
print(iris_df.tail())
print(iris_df(10))


print("\nGenerating beautiful graphs... Please check for the popup windows!")

# Graph 1: Pairplot 
# Shows relationships between all combinations of variables, colored by Species
pair_plot = sns.pairplot(iris_df, hue="Species", markers=["o", "s", "D"])
pair_plot.fig.suptitle("Pairplot of Iris Features", y=1.02)

# Graph 2: Violin Plot
# Shows the distribution and density of Petal Length for each Species
plt.figure(figsize=(10, 6))
sns.violinplot(x="Species", y="PetalLengthCm", data=iris_df, inner="quartile")
plt.title("Distribution of Petal Length by Species", fontsize=14)

# Graph 3: Joint KDE Plot
# A 2D density plot showing where the Sepal dimensions are clustered
joint_plot = sns.jointplot(
    data=iris_df,
    x="SepalLengthCm", y="SepalWidthCm", hue="Species",
    kind="kde", fill=True, alpha=0.7
)
joint_plot.fig.suptitle("Density of Sepal Dimensions", y=1.02)

# Display all the plots! (This will open them in separate windows)
plt.show()
