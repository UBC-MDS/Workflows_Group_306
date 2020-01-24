from docopt import docopt
import requests
import os
import pandas as pd


def main(url, out_file):

    
    
    # test url connection
    try: 
        request = requests.get(url)
        request.status_code == 200
    except Exception as req:
        print("Website at url is broken.")
        print(req)

    # get dataframe from url 
    data = pd.read_csv(url)

    # test for data type
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    if type(data) != type(df):
        raise Exception("Data file read in fail")

    # save df as csv, if file path doesnt exist, create file path
    try:
        print(os.getcwd())
        print(out_file)
        data.to_csv(out_file, index = False)
    except:
        os.makedirs(os.path.dirname(out_file))
        data.to_csv(out_file, index = False)

    try:
        pd.read_csv(out_file)
    except: 
        raise Exception("file save fail")

main(url = 'https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv',out_file = '../data/test_elo.csv')