import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_excel(r"C:\Users\SAMPATH\Desktop\SAMPATH PRODIGY TASK 1 EXECL FILE.xls")

# Check for duplicates and missing values
print("Number of duplicate rows:", df.duplicated().sum())
print("Number of missing values in each column:\n", df.isna().sum())

# Sort values by 'mean' and select the top 10
df_sorted = df.sort_values(by="mean", ascending=False).head(10)

# Extract the top 10 countries and their mean population
a = df_sorted["mean"].tail(10).tolist()
b = df_sorted["Country Name"].tail(10).tolist()

# Print the results
print("Top 10 countries by mean population:", b)
print("Mean population values:", a)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the bar plot
plt.figure(figsize=(12, 8))
colors = sns.color_palette("husl", len(a))  # Using a color palette from seaborn
plt.bar(b, a, color=colors)

# Add titles and labels
plt.title("Top 10 Countries by Mean Population (1990-2023)", fontsize=16)
plt.xlabel("Country Name", fontsize=10)
plt.ylabel("Mean Population", fontsize=10)
plt.xticks(rotation=45, ha="right")

# Improve layout and add grid
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()

