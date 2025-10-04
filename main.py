import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("EducationDataset_2023-24.csv")

# Quick check of columns
print(df.columns)

# -------------------
# 1. Scatter Plot
# Students (Total) vs No of Schools (Total)
# -------------------
plt.figure(figsize=(8,6))
plt.scatter(df["No of Schools - Total"], df["No of Students - Total"], alpha=0.6, color="blue")
plt.xlabel("Number of Schools (Total)")
plt.ylabel("Number of Students (Total)")
plt.title("Scatter Plot: Schools vs Students")
plt.grid(True)
plt.savefig("scatter_plot.png")
plt.show()

# -------------------
# 2. Box Plot
# Distribution of PASS % in Class X across Districts
# -------------------
plt.figure(figsize=(10,6))
df.boxplot(column=" PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24", grid=False)
plt.ylabel("Pass % in Class X (2023-24)")
plt.title("Box Plot: Distribution of Class X Pass %")
plt.savefig("box_plot.png")
plt.show()

# -------------------
# 3. Bar/Line Plot
# Pass Percentage in Class XII by District
# -------------------
plt.figure(figsize=(12,8))
plt.bar(df["District"], df["PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24"], color="green")
plt.xticks(rotation=90)
plt.xlabel("District")
plt.ylabel("Pass % in Class XII (2023-24)")
plt.title("Bar Plot: Class XII Pass % by District")
plt.savefig("bar_plot.png", bbox_inches="tight")  # 👈 fixes label cutoff
plt.show()

