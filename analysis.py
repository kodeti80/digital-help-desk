import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("issue_log.csv", names=["Time", "Text", "Category"])
category_counts = df["Category"].value_counts()
category_counts.plot(kind='bar', color='skyblue')
plt.title("Community Issue Report")
plt.xlabel("Issue Type")
plt.ylabel("Number of Reports")
plt.tight_layout()
plt.savefig("issue_summary.png")
plt.show()
