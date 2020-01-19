import pandas as pd

url1 = 'https://projects.fivethirtyeight.com/nfl-api/nfl_elo.csv'

url2 = 'https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv'



historic_df = pd.read_csv(url1)
current_df = pd.read_csv(url2)
#print(historic_df.head())

historic_df.to_csv("historic_nfl_elo.csv")
current_df.to_csv("current_nfl_elo.csv")