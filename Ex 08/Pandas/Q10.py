# Q10) Sports Tournament Data (dictionary + sorting + slicing)
# A sports event maintains player data in a dictionary with Player Name, Matches Played,
# and Runs Scored. Convert it into a DataFrame, sort players by Runs Scored in descending 
# order, and display the top 5 players.

import pandas as pd

# Dictionary with player data
data = {
    'Player Name': ['Virat Kohli', 'Rohit Sharma', 'Steve Smith', 'Kane Williamson', 
                   'Joe Root', 'David Warner', 'Babar Azam', 'Ben Stokes',
                   'Quinton de Kock', 'KL Rahul'],
    'Matches Played': [15, 18, 12, 14, 16, 13, 17, 15, 11, 14],
    'Runs Scored': [720, 845, 512, 678, 589, 623, 734, 456, 398, 567]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Sort by Runs Scored in descending order and get top 5 players
top = df.sort_values('Runs Scored', ascending=False).head(5)

# Display the result
print(top)

