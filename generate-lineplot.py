import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('./pitstops-data/pitstops-data.csv')

year = 2020

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

teams_to_include = ['Red Bull', 'Ferrari', 'Mercedes']  # adjust this list as needed

# Filter for the 2020 season, only include regular pit stops, and only include the specified teams
df = df[(df['SEASON'] == year) & (df['PIT_IRREGULAR'] == False) & (df['TEAM_SEASON'].isin(teams_to_include))]

df = df.sort_values(by='DATE')

# Group by the grand prix and team, and compute the average pit stop duration
grouped = df.groupby(['GRAND_PRIX', 'TEAM_SEASON'])['PIT_DUR'].mean()

# Unstack the grouped data to get a DataFrame where each column is a team and each row is a grand prix
unstacked = grouped.unstack()

# Sort the grand prix in chronological order
unstacked = unstacked.sort_index()

# Define a color map for the teams
color_map = {'Red Bull': 'red', 'Ferrari': 'green', 'Mercedes': 'blue'}
width_map = {'Red Bull': 2, 'Ferrari': 1, 'Mercedes': 1}

# Plot the DataFrame
plt.figure(figsize=(15, 10))
for team in unstacked.columns:
    plt.plot(unstacked.index, unstacked[team], label=team, color=color_map[team], linewidth=width_map[team])

plt.xticks(rotation=90)
plt.xlabel(f'{year}')
plt.ylabel('Average Pit Stop Time (seconds)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.title('Average Pit Stop Time by Team across Grand Prix')
plt.tight_layout()
plt.ylim(1.7,5)
plt.show()
