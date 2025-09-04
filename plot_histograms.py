import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('./Data_folder/clean&merge_data.csv')

# Create histograms
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Histogram for age
axes[0].hist(df['age'], bins=20, edgecolor='black')
axes[0].set_title('Age Distribution')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Frequency')

# Histogram for income
axes[1].hist(df['income'], bins=20, edgecolor='black')
axes[1].set_title('Income Distribution')
axes[1].set_xlabel('Income')
axes[1].set_ylabel('Frequency')

plt.tight_layout()

# Save the plot
plt.savefig('histograms.png')
plt.show()
