# Author: Tani Barasch
# date: 2020-23-01

"""Downloads data csv from the web to a local filepath as a csv file format.
Usage: src/down_data.py --url=<url> --out_file=<out_file>
Options:
--url=<url>              URL from where to download the data (must be in standard csv format)
--out_file=<out_file>    Path (including filename) of where to locally write the file
"""

from docopt import docopt
import requests
import os
import pandas as pd

url1 = 'https://projects.fivethirtyeight.com/nfl-api/nfl_elo.csv'
url2 = 'https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv'


opt = docopt(__doc__)

def main(url, out_file):
    
    # test url
    try: 
        request = requests.get(url)
        request.status_code == 200
    except Exception as req:
        print("Website at url is broken.")
        print(req)

    # get dataframe from url 
    data = pd.read_csv(url, )

    # save df as csv
    try:
        data.to_csv(out_file, index = False)
    except:
        os.makedirs(os.path.dirname(out_file))
        data.to_csv(out_file, index = False)

# call main function
if __name__ == "__main__":
    main(opt["--url"],opt["--out_file"])