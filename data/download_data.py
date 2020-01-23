


url1 = 'https://projects.fivethirtyeight.com/nfl-api/nfl_elo.csv'

url2 = 'https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv'
historic_df = pd.read_csv(url1)
current_df = pd.read_csv(url2)

def main(url,file_name, path):

# documentation comments

# import libraries/packages
    import pandas as pd

# parse/define command line arguments here

# define main function
    path = "../data"
    df = pd.read_csv(url)
    df.to_csv("historic_nfl_elo.csv")
    current_df.to_csv("current_nfl_elo.csv")
    # code for "guts" of script goes here

# code for other functions & tests goes here

# call main function
if __name__ == "__main__":
    main()