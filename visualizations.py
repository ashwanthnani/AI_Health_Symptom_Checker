import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Disease Count
disease_count = df["Disease"].value_counts()

# Bar Chart
plt.figure(figsize=(8,5))
disease_count.plot(kind="bar")
plt.title("Disease Frequency")
plt.xlabel("Disease")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("disease_chart.png")
plt.show()

# Pie Chart
plt.figure(figsize=(7,7))
disease_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Disease Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("disease_pie_chart.png")
plt.show()

print("Charts Generated Successfully!")