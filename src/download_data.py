# Author: Tani Barasch
# date: 2020-23-01

"""Downloads data csv from the web to a local filepath as a csv file format.

Usage: src/download_data.py --url=<url> --out_file=<out_file>

Options:
--url=<url>              URL from where to download the data (must be in standard csv format)
--out_file=<out_file>    Path (including filename) of where to locally write the file
"""

from docopt import docopt
import requests
import os
import pandas as pd

# historic data url: https://projects.fivethirtyeight.com/nfl-api/nfl_elo.csv
# 2019 data url:     https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv

# full command for each file:
#  python src/download_data.py --url="https://projects.fivethirtyeight.com/nfl-api/nfl_elo.csv" --out_file="data/elo_historic_raw.csv"
#  python src/download_data.py --url="https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv" --out_file="data/elo_2019_raw.csv"


opt = docopt(__doc__)

def main(url, out_file): 
    
    # test url connection
    try: 
        request = requests.get(url)
        request.status_code == 200
    except Exception as req:
        print("Website at url is broken.")
        print(req)
        
    data = pd.read_csv(url)

    # test for data type
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    if type(data) != type(df):
        raise Exception("Data file read in fail")

    # save df as csv, if file path doesnt exist, create file path
    try:
        data.to_csv(out_file)
    except:
        os.makedirs(os.path.dirname(out_file))
        data.to_csv(out_file, index = False)

    try:
        pd.read_csv(out_file)
    except: 
        raise Exception("file save fail")

#main('https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv','../data/elo_test.csv')



# call main function
if __name__ == "__main__":
    main(opt["--url"], opt["--out_file"])