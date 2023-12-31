# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kdb-omCdEjE63U8zQmU7iZw8YfRaqp-1
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load datasets
games = pd.read_csv('games.csv')
games_details = pd.read_csv('games_details.csv', low_memory=False)
players = pd.read_csv('players.csv')
ranking= pd.read_csv('ranking.csv')
teams = pd.read_csv('teams.csv')

# Display basic information about each dataset
print("Games Dataset:")
print(games.info())
print("\nGames Details Dataset:")
print(games_details.info())
print("\nPlayers Dataset:")
print(players.info())
print("\nRanking Dataset:")
print(ranking.info())
print("\nTeams Dataset:")
print(teams.info())

print(games.describe())

# Plot a bar chart of team wins
import numpy as np
wl_group = games.groupby(['HOME_TEAM_WINS'])

win_filt = wl_group.get_group(1)
lose_filt = wl_group.get_group(0)

# do teams perform better when at home stadium?
#groupings and bar plot
x = win_filt['HOME_TEAM_WINS'].value_counts()
y = lose_filt['HOME_TEAM_WINS'].value_counts()

ti = [0.5]
hor = np.arange(len(ti))

plt.bar(ti,x,width = 0.25,color = '#0077b6',label = 'Home Games')
plt.bar(hor + 0.75,y,width = 0.25,color = '#fb8500',label = 'Away Games')

plt.ylabel('Number of Wins')
plt.xticks(color = 'w')
plt.title('Win comparison between Home and Away Games')
plt.legend()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'games_df' is the DataFrame with information about each game
# Assuming 'SEASON_x' is the column indicating the season
# Assuming 'HOME_TEAM_WINS' is the column indicating whether the home team wins (1 for Yes, 0 for No)

# Group by season and home wins
season_wise_wins = games.groupby(['SEASON', 'HOME_TEAM_WINS']).size().unstack()

# Plotting line plot for home wins vs. away wins over seasons
plt.figure(figsize=(10, 6))

# Use a line plot to show the trend
sns.lineplot(data=season_wise_wins, x='SEASON', y=1, marker='o', label='Home Wins', color='#0077b6')
sns.lineplot(data=season_wise_wins, x='SEASON', y=0, marker='o', label='Away Wins', color='#fb8500')

plt.xlabel('Season')
plt.ylabel('Number of Wins')

plt.title('Season-wise Win Comparison between Home and Away Games')
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Example criteria for clutch situations: games with a score difference of 5 points or less in the last 5 minutes
clutch_games = games[(abs(games['PTS_home'] - games['PTS_away']) <= 5) & (games['GAME_STATUS_TEXT'] == 'Final')]
clutch_game_ids = clutch_games['GAME_ID'].unique()

# Subset relevant columns from games_details
required_columns_details = ['GAME_ID', 'PLAYER_ID', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'MIN']
games_details_subset = games_details[required_columns_details]

# Handling missing values in each dataset
games.dropna(inplace=True)
players.dropna(inplace=True)
games_details_subset.dropna(inplace=True)

# Merge datasets
merged_data = pd.merge(games, games_details_subset, left_on='GAME_ID', right_on='GAME_ID')
merged_data = pd.merge(merged_data, players, left_on='PLAYER_ID', right_on='PLAYER_ID')

# Define clutch players based on your criteria (e.g., players with high points in clutch situations)
clutch_players = merged_data.groupby('PLAYER_NAME')['PTS'].sum().nlargest(5).index

# Filter data for clutch players
clutch_players_data = merged_data[merged_data['PLAYER_NAME'].isin(clutch_players)]

# Visualize clutch performance metrics
plt.figure(figsize=(12, 8))
sns.barplot(data=clutch_players_data, x='PLAYER_NAME', y='PTS', hue='GAME_STATUS_TEXT')
plt.xlabel('Player')
plt.ylabel('Points')
plt.title('Clutch Performance Analysis: Points in Clutch Situations')
plt.legend(title='Game Status')
plt.show()

# Plot a bar chart of the number of teams in each city
team_city_counts = teams['CITY'].value_counts()
plt.figure(figsize=(12, 6))
team_city_counts.plot(kind='bar', color='orange')
plt.title('Number of Teams in Each City')
plt.xlabel('City')
plt.ylabel('Number of Teams')
plt.xticks(rotation=45)
plt.show()

