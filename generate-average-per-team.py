import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('./pitstops-data/pitstops-data.csv')

# Filter the DataFrame to only include rows for the Australian Grand Prix
australian_gp = df[(df['SEASON'] == 2018) & (df['GRAND_PRIX'] == 'Australian Grand Prix')]

# Group the DataFrame by team and calculate the mean pit stop duration
team_pit_stops = australian_gp.groupby('TEAM_SEASON')['PIT_DUR'].mean()

# Sort the results from fastest to slowest
team_pit_stops = team_pit_stops.sort_values()

# Format the pit stop durations with two digits after the decimal point
team_pit_stops = team_pit_stops.apply(lambda x: round(x, 2))
team_pit_stops = team_pit_stops.apply(lambda x: '{:.2f}'.format(x))

# Print the results
print(team_pit_stops)