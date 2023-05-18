import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('./pitstops-data/pitstops-data2.csv')

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Filter out irregular pit stops
df = df[df['PIT_IRREGULAR'] == False]

# Group by circuit and calculate the average pit stop duration
grouped = df.groupby('CIRCUIT')['PIT_DUR'].mean()

# Convert the grouped data to a DataFrame
circuit_averages = pd.DataFrame(grouped).reset_index()

# Sort the circuits by average pit stop duration
circuit_averages = circuit_averages.sort_values(by='PIT_DUR')

# Plot the results
plt.figure(figsize=(10, 6))
sns.barplot(x='PIT_DUR', y='CIRCUIT', data=circuit_averages, palette='viridis')

# Set plot configurations
plt.xlabel('Average Pit Stop Time (seconds)', fontsize=14)
plt.ylabel('Circuit', fontsize=14)
plt.title('Average Pit Stop Time per Circuit', fontsize=16, y=1.05)

# Render the plot
plt.tight_layout()
plt.show()
