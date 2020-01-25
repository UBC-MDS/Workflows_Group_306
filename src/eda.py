""" Runs classification model on the cleaned data to get the accuarcy on the test results

Usage: src/eda.py --source=<source> --correlation=<correlation> --elo_win=<elo_win> --eda_score=<eda_score>

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from numpy.polynomial.polynomial import polyfit
import heatmap_func as hp
from docopt import docopt

opt = docopt(__doc__)

def main(source, correlation, elo_win, eda_score):
  # source = "../data/elo_historic_raw.csv"
  df = pd.read_csv(source).set_index("Unnamed: 0")
  
  corr = df.corr()
  ylabels = list(corr.index)
  xlabels = list(corr.columns)
  
  corr_arr = np.array(corr)
  corr_arr = np.round(corr_arr, 1)
  
  fig, ax = plt.subplots()
  plt.rcParams["figure.figsize"] = [500, 500]
  plt.rcParams.update({'font.size': 5})
  
  im, cbar = hp.heatmap(corr_arr, ylabels, xlabels, ax=ax,
                     cmap="YlGn", cbarlabel="correlation")
  texts = hp.annotate_heatmap(im, valfmt=" {x:.1f} ")
  
  fig.tight_layout()
  # correlation = '../img/eda-heatmap_for_correlations.png'
  fig.savefig(correlation, dpi=200)
  # plt.show()
  
  eda_cols = ['season', 'playoff', 'elo1_pre', 'elo2_pre', 'elo_prob1', 'elo_prob2', 'elo1_post', 'elo2_post', 'qbelo1_pre', 'qbelo2_pre', 'qbelo_prob1', 'qbelo_prob2', 'score1', 'score2']

  df_table = df[eda_cols]
  df_table['decade'] = (df_table["season"]//10)*10
  df_xs_reg = df_table.query('season > 1969 & season < 2019')
  df_xs_reg.loc[:, 'elo_diff'] = df_xs_reg['elo1_pre'] - df_xs_reg['elo2_pre']
  df_xs_reg.loc[:, 'score_diff'] = df_xs_reg['score1'] - df_xs_reg['score2']
  df_xs_reg.loc[:, 'is_winner'] = np.where(df_xs_reg['score_diff'] > 0, 1, 0)
  df_xs_reg.loc[:, 'elo_change_aftergame'] = df_xs_reg['elo1_post'] - df_xs_reg['elo1_pre']
  
  conditions = [
    (df_xs_reg['elo_diff'] > 0) & (df_xs_reg['score_diff'] > 0),
    (df_xs_reg['elo_diff'] < 0) & (df_xs_reg['score_diff'] > 0),
    (df_xs_reg['elo_diff'] > 0) & (df_xs_reg['score_diff'] < 0),
    (df_xs_reg['elo_diff'] < 0) & (df_xs_reg['score_diff'] < 0),
    (df_xs_reg['elo_diff'] < 0) & (df_xs_reg['score_diff'] == 0),
    (df_xs_reg['elo_diff'] > 0) & (df_xs_reg['score_diff'] == 0)
  ]
  choices = [
    'high_elo_win', 'low_elo_win', 'high_elo_lose', 'low_elo_lose', 'low_elo_tie', 'high_elo_tie'
  ]
  df_xs_reg['elo_vs_result'] = np.select(conditions, choices, default = 'not_sure')
  print("** Start doing warn")
  elo_vs_result = df_xs_reg.groupby('elo_vs_result')['elo_vs_result'].count()
  # elo_win = ../data/eda-elo_vs_result.csv
  elo_vs_result.to_csv(elo_win, header = False)
  
  print("** finish saving csv")
  
  df_xs_reg = df_table.query('season > 1969 & season < 2019')
  df_xs_reg.loc[:, 'elo_diff'] = df_xs_reg['elo1_pre'] - df_xs_reg['elo2_pre']
  df_xs_reg.loc[:, 'score_diff'] = df_xs_reg['score1'] - df_xs_reg['score2']
  df_xs_reg.loc[:, 'is_winner'] = np.where(df_xs_reg['score_diff'] > 0, 1, 0)
  df_xs_reg.loc[:, 'elo_change_aftergame'] = df_xs_reg['elo1_post'] - df_xs_reg['elo1_pre']
  df_xs_reg
  
  print("** finish wrangling")
  
  x = np.array(df_xs_reg['elo_diff'])
  y = np.array(df_xs_reg['score_diff'])
  y0, m = polyfit(x, y, 1)
  
  x2 = np.array(df_xs_reg['elo_change_aftergame'])
  y2 = np.array(df_xs_reg['score_diff'])
  c2 = np.array(df_xs_reg['is_winner'])
  
  print("** ready to plot")
  fig2, ax = plt.subplots()
  plt.rcParams["figure.figsize"] = [200, 200]
  ax.scatter(x, y, alpha = 0.2)
  ax.plot(x, y0 + m * x, color='red')
  print("** here i am")
  ax.set(xlabel='difference in ELO', 
          ylabel='difference in score', title = 'Score vs pre-game ELO')
  # ax.legend()
  # ax.grid()
  # fig2.tight_layout()
  # eda_score = "../img/eda-score_vs_pregame_elo.png"
  print("** ready to save")
  fig2.savefig(eda_score, dpi = 200)
  print("** plot saved")
  # plt.show()
  
  
if __name__ == "__main__":
    main(opt["--source"], opt["--correlation"], opt["--elo_win"], opt["--eda_score"])
