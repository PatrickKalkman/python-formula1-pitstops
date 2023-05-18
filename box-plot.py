import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('./pitstops-data/pitstops-data.csv')

year = 2020

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

teams_to_include = ['Red Bull', 'Ferrari', 'Mercedes', 'Williams', 'Renault', 'McLaren', 'Alfa Romeo', 'Haas', 'AlphaTauri']  # adjust this list as needed

# Filter for the 2020 season, only include regular pit stops, and only include the specified teams
df = df[(df['SEASON'] == year) & (df['PIT_IRREGULAR'] == False) & (df['TEAM_SEASON'].isin(teams_to_include))]

df = df.sort_values(by='DATE')

# Set a theme for the plot
sns.set_theme(style="whitegrid")

# Create a color palette
palette = sns.color_palette("hls", len(teams_to_include))

plt.figure(figsize=(15, 10))

# Create boxplot
sns.boxplot(x='TEAM_SEASON', y='PIT_DUR', data=df, order=teams_to_include, palette=palette)
#sns.violinplot(x='TEAM_SEASON', y='PIT_DUR', data=df, order=teams_to_include)


# Add title and labels
plt.title(f'Pit Stop Duration by Team in the {year} Season', fontsize=20)
plt.xlabel('Team', fontsize=15)
plt.ylabel('Pit Stop Duration (seconds)', fontsize=15)
plt.ylim(2,5)
plt.show()
