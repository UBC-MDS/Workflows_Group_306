""" Runs classification model on the cleaned data to get the accuarcy on the test results

Usage: src/eda2.py --source=<source> --correlation=<correlation> --elo_win=<elo_win> --eda_score=<eda_score> --result_elo=<result_elo>

"""

import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from numpy.polynomial.polynomial import polyfit
import heatmap_func as hp
from docopt import docopt

opt = docopt(__doc__)

# calling example
# python src/eda2.py --source=data/elo_historic_raw.csv --correlation=img/eda-heatmap_for_correlations.png --elo_win=data/eda-elo_vs_result.csv --eda_score=img/elo_lnrg.png --result_elo=img/elo_change.png

def main(source, correlation, elo_win, eda_score, result_elo):
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
  
  alt.data_transformers.disable_max_rows()

  base = alt.Chart(df_xs_reg).mark_circle(opacity = 0.5).encode(
      alt.X('elo_diff:Q', title = 'Difference in elo (home - away)'),
      alt.Y('score_diff:Q', title = 'Difference in scores (home - away)')
  ).properties(
      title = 'Diff in score vs diff in ELO',# hopefully I call this right
      height = 600,
      width = 800
  )
  
  order = 1
  lin_fit = base.transform_regression(
      'elo_diff', 'score_diff', method = 'poly', order = order, as_ = ['elo_diff', str(order)]
  ).mark_line(color = 'red').transform_fold(
      [str(order)], as_ = ['degree', 'score_diff']
  ).encode()
  
  chart = alt.layer(base, lin_fit)
  chart.save(eda_score)
  
  p2 = alt.Chart(df_xs_reg).mark_point().encode(
    alt.Y("elo_change_aftergame:Q", title = 'ELO change after game'),
    alt.X("score_diff:Q", title = 'difference in score'),
    alt.Color('is_winner:O')
  ).properties(
    title = 'Game result change ELO',# hopefully I call this right
      height = 600,
      width = 800
  )
  
  p2.save(result_elo)
  
  
if __name__ == "__main__":
    main(opt["--source"], opt["--correlation"], opt["--elo_win"], opt["--eda_score"], opt["--result_elo"])
