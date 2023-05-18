import json
from collections import defaultdict

# Open the JSON file
with open('./pitstops-data/pitstop-2022-3.json') as f:
    race_data = json.load(f)

# Open the teams file
with open('./pitstops-data/teams-2022.json') as f:
    team_data = json.load(f)

# Initialize a dictionary to hold total duration and count for each team
team_durations = defaultdict(lambda: {"total": 0, "count": 0})

# Initialize a dictionary to map driver IDs to their teams
driver_teams = {}

# Populate the driver_teams dictionary from the teams data
for team in team_data['teams']:
    team_name = team['name']
    for driver in team['drivers']:
        driver_teams[driver['driverId']] = team_name

# Iterate over pit stops
for pit_stop in race_data['MRData']['RaceTable']['Races'][0]['PitStops']:
    # Extract team and duration
    driver_id = pit_stop['driverId']
    duration = float(pit_stop['duration'])

    # Get the team name from the driver ID
    team = driver_teams.get(driver_id, "Unknown team")
    if team == "Unknown team":
        print(driver_id)

    # Update total duration and count for the team
    team_durations[team]['total'] += duration
    team_durations[team]['count'] += 1

# Calculate and print average duration for each team
average_durations = []
for team, data in team_durations.items():
    average_duration = data['total'] / data['count']
    average_durations.append((team, average_duration))

# Sort the list of tuples by average duration
average_durations.sort(key=lambda x: x[1])

# Print the sorted average durations
for team, average_duration in average_durations:
    print(f"Average pit stop duration for {team}: {average_duration:.2f} seconds")
