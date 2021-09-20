import pandas as pd

pd.options.display.max_columns = 25

# load in data file #
df = pd.read_csv('deep_learning_data.csv')

df.head()
df.shape
df.tail(10)

df.loc[3]   # select a row (3th)
df.loc[3,'player']      # select [3,player]

#   return entire column
df.loc[:,'player']
df['player']
df.player

#select rows/ columns according to conditions

df.loc[(df.player == 'MrBlue') & (df.hand == 0)]
df.loc[(df.player == 'MrBlue') & (df.hand == 0)].shape
df_blue_firsthand = df.loc[(df.player == 'MrBlue') & (df.hand == 0)]
df_blue_firsthand.shape

df.head()
df['sum_slansky_seat'] = df['slansky'] + df.seat


df_con = df.loc[((df.slansky == 9) | (df.slansky == 7)) & (df.seat == 2),['player','slansky','seat']]
df_con.shape


#   special column operations
average_by_game_hand = df.groupby(['game','hand']).slansky.mean()
average_by_game_hand.head()
average_by_game_hand.loc[(94,0)]

print(average_by_game_hand.loc[(94,0)])
