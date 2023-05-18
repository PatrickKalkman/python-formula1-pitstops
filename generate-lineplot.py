import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style for enhanced aesthetics
sns.set_theme()

# Load the data
df = pd.read_csv('./pitstops-data/pitstops-data.csv')

year = 2018

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

teams_to_include = ['Red Bull', 'Ferrari', 'Mercedes']  # adjustable team list

# Filter for the 2018 season, include only regular pit stops, and select the specified teams
df = df[(df['SEASON'] == year) & (df['PIT_IRREGULAR'] == False) & (df['TEAM_SEASON'].isin(teams_to_include))]

# Sort the DataFrame by date
df = df.sort_values(by='DATE')

# Group by the grand prix and team, calculate the average pit stop duration
grouped = df.groupby(['GRAND_PRIX', 'TEAM_SEASON'])['PIT_DUR'].mean()

# Convert the grouped data into a DataFrame where each column is a team, and each row represents a grand prix
unstacked = grouped.unstack()

# Sort the grand prix in chronological order
unstacked = unstacked.sort_index()

# Define a color map for the teams
color_map = {'Red Bull': 'mediumblue', 'Ferrari': 'crimson', 'Mercedes': 'gray'}
width_map = {'Red Bull': 2.5, 'Ferrari': 1, 'Mercedes': 1}

# Initialize the plot
plt.figure(figsize=(15, 10))
for team in unstacked.columns:
    plt.plot(unstacked.index, unstacked[team], label=team, color=color_map[team], linewidth=width_map[team])

# Set plot configurations
plt.xticks(rotation=45)
plt.xlabel(f'Grand Prix - {year}', fontsize=14)
plt.ylabel('Average Pit Stop Time (seconds)', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Teams', title_fontsize='13', fontsize='12')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.title('Average Pit Stop Time by Team across Grand Prix', fontsize=16, y=1.05)
plt.tight_layout()
plt.ylim(1.7,5)

# Render the plot
plt.show()
