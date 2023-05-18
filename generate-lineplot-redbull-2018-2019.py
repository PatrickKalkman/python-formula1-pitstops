import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style for enhanced aesthetics
sns.set_theme()

# Load the data
df = pd.read_csv('./pitstops-data/pitstops-data.csv')

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Extract the year from 'DATE' to a new column 'SEASON'
df['SEASON'] = df['DATE'].dt.year

team = 'Red Bull'  # specify the team

# Filter to include only regular pit stops, select the specified team, and exclude the 2020 season
df = df[(df['PIT_IRREGULAR'] == False) & (df['TEAM_SEASON'] == team) & (df['SEASON'] != 2020)]

# Sort the DataFrame by date
df = df.sort_values(by='DATE')

# Group by the season, grand prix and team, then calculate the average pit stop duration
grouped = df.groupby(['SEASON', 'GRAND_PRIX', 'TEAM_SEASON'])['PIT_DUR'].mean()

# Convert the grouped data into a DataFrame where each column is a season, and each row represents a grand prix
unstacked = grouped.unstack(level=0)

# Define a color map for the seasons
color_map = {season: ('red' if season % 2 == 0 else 'blue') for season in unstacked.columns}

# Increase line width
line_width = 2.5

# Initialize the plot
plt.figure(figsize=(15, 10))
for season in unstacked.columns:
    plt.plot(unstacked.index.get_level_values('GRAND_PRIX'), unstacked[season], label=season, color=color_map[season], linewidth=line_width)

# Set plot configurations
plt.xticks(rotation=45)
plt.xlabel('Grand Prix', fontsize=14)
plt.ylabel('Average Pit Stop Time (seconds)', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Seasons', title_fontsize='13', fontsize='12')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.title(f'Average Pit Stop Time by {team} across Seasons', fontsize=16, y=1.05)
plt.tight_layout()
plt.ylim(1.7,5)

# Render the plot
plt.show()
