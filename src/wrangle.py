# Author: Tani Barasch
# date: 2020-23-01

"""This script wrangles the elo csv file to useable data.
remove all years prior to 1970 (NFL merger)
get rid of NA
writes wrangled csv to specified path

Usage: src/wrangle.py --input=<input> --out_dir=<out_dir>

Options:
--input=<input>       Path (including filename) to raw data (csv file)
--out_dir=<out_dir>   Path to directory where the processed data should be written including name.
"""

from docopt import docopt
import requests
import os
import pandas as pd
import numpy as np

# full command for each file:
#  python src/wrangle.py --input="data/elo_historic_raw.csv" --out_dir="data/elo_historic_wrangled.csv"
#  python src/wrangle.py --url="data/elo_2019_raw.csv" --out_dir="data/elo_2019_wrangled.csv"

opt = docopt(__doc__)

def main(input,out_dir):

    def count_nan(df):
        """
        counts rows in which there is an NAN value.
        run time of O(d*n)
        """
        count = 0
        for i in range(len(df.index)) :
            if df.iloc[i].isnull().sum() > 0:
                count +=1
        return count

    def win(df):
        """
        find winner per row based on score1 vs score2 columns
        """
        if df['score1'] == df['score2']:
            val = 'tie'
        elif df['score1'] > df['score2']:
            val = 'winner'
        else:
            val = 'loser'
        return val

    def test_win():
        """
        test df post use of win() by checking no. of unique vals and that all rows are assigned
        """
        if df['status'].nunique(dropna = True) > 3:
            raise Exception("Unexpected winner outcome")
        #for i in range(len(df.index)): 
            #if pd.notnull(df['score1'].iloc[i]) and pd(notnull(df['score2'].iloc[i].isna()):
            #    if False == pd.notnull(df['status'].iloc[i]):
            #        raise Exception('failed to determine all winners')
    
    df = pd.read_csv(input)

    # filter all NFL seasons prior to 1970 (AFL-NFL merger)
    df = df.loc[df["season"] >= 1970].iloc[:,1:]

    # drop cols with "post" in name
    df = df.drop(df.filter(regex='post').columns, axis=1)
    # drop cols with team or QB name in them
    df = df.drop(df.filter(regex='team').columns, axis=1).drop(['qb1','qb2'], axis=1)
    # drop other uneeded columns
    df = df.drop(['playoff','date','qb1_adj','qb2_adj'],axis=1)
    
    df = df.dropna()
    if count_nan(df) != 0:
        raise Exception('failed to drop NAN values')
    # create column with winner per row
    df['status'] = df.apply(win, axis = 1)
    test_win()
    # drop score cols and all rows still with na
    df = df.drop(['score1','score2'],axis=1)



    try:
        df.to_csv(out_dir, index = False)
    except:
        os.makedirs(os.path.dirname(out_dir))
        df.to_csv(out_dir, index = False)

    # testing if file was written properly
    try:
        pd.read_csv(out_dir)
    except: 
        raise Exception("file save fail")

# call main function
if __name__ == "__main__":
    main(opt["--input"], opt["--out_dir"])

