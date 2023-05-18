import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict

# Function to convert duration string to seconds
def duration_to_seconds(duration_str):
    mins, secs = duration_str.split(':')
    return float(mins) * 60 + float(secs)

# Open the teams file
with open('./pitstops-data/teams-2022.json') as f:
    team_data = json.load(f)

# Initialize a dictionary to map driver IDs to their teams
driver_teams = {}

# Populate the driver_teams dictionary from the teams data
for team in team_data['teams']:
    team_name = team['name']
    for driver in team['drivers']:
        driver_teams[driver['driverId']] = team_name

# Create an empty DataFrame to hold the average pit stop durations for each team in each race
df = pd.DataFrame()

# Loop over all the races
for race in range(1, 23):  # Assumes races are numbered from 1 to 22
    # Open the JSON file for the current race
    with open(f'./pitstops-data/pitstop-2022-{race}.json') as f:
        race_data = json.load(f)

    # Initialize a dictionary to hold total duration and count for each team
    team_durations = defaultdict(lambda: {"total": 0, "count": 0})

    # Iterate over pit stops
    for pit_stop in race_data['MRData']['RaceTable']['Races'][0]['PitStops']:
        # Extract team and duration
        driver_id = pit_stop['driverId']
        duration_string = pit_stop['duration']
        if ':' in duration_string:
            continue
        duration = float(pit_stop['duration'])

        # Get the team name from the driver ID
        team = driver_teams.get(driver_id, "Unknown team")
        if team == "Unknown team":
            print(driver_id)

        # Update total duration and count for the team
        team_durations[team]['total'] += duration
        team_durations[team]['count'] += 1

    # Calculate average duration for each team and store in a temporary DataFrame
    avg_durations = {}
    for team, data in team_durations.items():
        avg_durations[team] = data['total'] / data['count']

    temp_df = pd.DataFrame(avg_durations, index=[race])

    # Append the temporary DataFrame to the main DataFrame
    df = df.append(temp_df)

# Plot the heatmap
plt.figure(figsize=(10, 8))  # Adjust as needed
sns.heatmap(df, cmap='seismic', cbar_kws={'label': 'Average Pit Stop Duration'})
plt.title('Average Pit Stop Duration per Team per Race')
plt.xlabel('Team')
plt.ylabel('Race')
plt.show()
