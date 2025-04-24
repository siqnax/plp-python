
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset

# Load the Iris dataset from seaborn for convenience
df = sns.load_dataset("iris")

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check the structure of the dataset
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# No missing values to clean in this dataset, but if there were:
# df = df.dropna() or df.fillna(value)

# Task 2: Basic Data Analysis

# Basic statistics
print("\nDescriptive statistics:")
print(df.describe())

# Grouping by species and calculating mean of numerical columns
grouped = df.groupby("species").mean()
print("\nMean values grouped by species:")
print(grouped)

# Observation
print("\nObservation: Setosa has noticeably smaller measurements compared to Virginica and Versicolor.")

# Task 3: Data Visualization

# Set a consistent style
sns.set(style="whitegrid")

# 1. Line chart - simulate a trend using index vs petal length
plt.figure(figsize=(10, 4))
plt.plot(df.index, df['petal_length'], label='Petal Length')
plt.title("Petal Length Trend Over Sample Index")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length")
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar chart - average petal length per species
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="species", y="petal_length")
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length")
plt.tight_layout()
plt.show()

# 3. Histogram - distribution of sepal width
plt.figure(figsize=(6, 4))
plt.hist(df['sepal_width'], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter plot - sepal length vs petal length
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species')
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend(title="Species")
plt.tight_layout()
plt.show()
