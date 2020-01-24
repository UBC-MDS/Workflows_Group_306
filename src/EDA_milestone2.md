Untitled
================

## The information about columns

    ## <class 'pandas.core.frame.DataFrame'>
    ## Int64Index: 16541 entries, 0 to 16540
    ## Data columns (total 30 columns):
    ## date              16541 non-null object
    ## season            16541 non-null int64
    ## neutral           16541 non-null int64
    ## playoff           577 non-null object
    ## team1             16540 non-null object
    ## team2             16540 non-null object
    ## elo1_pre          16540 non-null float64
    ## elo2_pre          16540 non-null float64
    ## elo_prob1         16540 non-null float64
    ## elo_prob2         16540 non-null float64
    ## elo1_post         16538 non-null float64
    ## elo2_post         16538 non-null float64
    ## qbelo1_pre        14376 non-null float64
    ## qbelo2_pre        14376 non-null float64
    ## qb1               14378 non-null object
    ## qb2               14378 non-null object
    ## qb1_value_pre     14378 non-null float64
    ## qb2_value_pre     14378 non-null float64
    ## qb1_adj           14379 non-null float64
    ## qb2_adj           14379 non-null float64
    ## qbelo_prob1       14378 non-null float64
    ## qbelo_prob2       14378 non-null float64
    ## qb1_game_value    14376 non-null float64
    ## qb2_game_value    14376 non-null float64
    ## qb1_value_post    14376 non-null float64
    ## qb2_value_post    14376 non-null float64
    ## qbelo1_post       14376 non-null float64
    ## qbelo2_post       14376 non-null float64
    ## score1            16538 non-null float64
    ## score2            16538 non-null float64
    ## dtypes: float64(22), int64(2), object(6)
    ## memory usage: 3.9+ MB

## Correlation between columns

<img src="/home/franklu/MDS/Workflows_Group_306/src/EDA_milestone2_files/figure-gfm/correlation heatmap-1.png" width="672" />

## Because of the major rule change effective in 1970, remove data points before 1970

    ## /home/franklu/anaconda3/bin/python:1: SettingWithCopyWarning: 
    ## A value is trying to be set on a copy of a slice from a DataFrame.
    ## Try using .loc[row_indexer,col_indexer] = value instead
    ## 
    ## See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

    ## /home/franklu/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py:376: SettingWithCopyWarning: 
    ## A value is trying to be set on a copy of a slice from a DataFrame.
    ## Try using .loc[row_indexer,col_indexer] = value instead
    ## 
    ## See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    ##   self.obj[key] = _infer_fill_value(value)
    ## /home/franklu/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py:494: SettingWithCopyWarning: 
    ## A value is trying to be set on a copy of a slice from a DataFrame.
    ## Try using .loc[row_indexer,col_indexer] = value instead
    ## 
    ## See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    ##   self.obj[item] = s

    ## /home/franklu/anaconda3/bin/python:1: FutureWarning: The signature of `Series.to_csv` was aligned to that of `DataFrame.to_csv`, and argument 'header' will change its default value from False to True: please pass an explicit value to suppress this warning.

    ##             season playoff     elo1_pre     elo2_pre  elo_prob1  elo_prob2  ...  decade    elo_diff  score_diff  is_winner  elo_change_aftergame  elo_vs_result
    ## Unnamed: 0                                                                  ...                                                                                
    ## 4549          1970     NaN  1583.202000  1426.127000   0.782172   0.217828  ...    1970  157.075000        21.0          1             12.232000   high_elo_win
    ## 4550          1970     NaN  1475.119000  1382.173000   0.712839   0.287161  ...    1970   92.946000        -8.0          0            -33.748000  high_elo_lose
    ## 4551          1970     NaN  1396.972000  1638.776000   0.265463   0.734537  ...    1970 -241.804000        10.0          1             38.305000    low_elo_win
    ## 4552          1970     NaN  1458.876000  1488.866000   0.550214   0.449786  ...    1970  -29.990000         9.0          1             20.389000    low_elo_win
    ## 4553          1970     NaN  1386.799000  1436.731000   0.521671   0.478329  ...    1970  -49.932000       -15.0          0            -29.127000   low_elo_lose
    ## ...            ...     ...          ...          ...        ...        ...  ...     ...         ...         ...        ...                   ...            ...
    ## 16269         2018       d  1640.171960  1647.624483   0.582068   0.417932  ...    2010   -7.452523        13.0          1             21.496606    low_elo_win
    ## 16270         2018       d  1669.105861  1633.114673   0.641378   0.358622  ...    2010   35.991188         6.0          1             13.344334   high_elo_win
    ## 16271         2018       c  1682.450194  1648.424105   0.638772   0.361228  ...    2010   34.026089        -3.0          0            -18.545290  high_elo_lose
    ## 16272         2018       c  1675.286412  1661.668566   0.611248   0.388752  ...    2010   13.617846        -6.0          0            -24.670271  high_elo_lose
    ## 16273         2018       s  1666.969395  1686.338837   0.472154   0.527846  ...    2010  -19.369442       -10.0          0            -22.445895   low_elo_lose
    ## 
    ## [11725 rows x 20 columns]

## Plot for season games

    ##             season playoff     elo1_pre     elo2_pre  elo_prob1  elo_prob2  ...  score2  decade    elo_diff  score_diff  is_winner  elo_change_aftergame
    ## Unnamed: 0                                                                  ...                                                                         
    ## 4549          1970     NaN  1583.202000  1426.127000   0.782172   0.217828  ...    13.0    1970  157.075000        21.0          1             12.232000
    ## 4550          1970     NaN  1475.119000  1382.173000   0.712839   0.287161  ...    24.0    1970   92.946000        -8.0          0            -33.748000
    ## 4551          1970     NaN  1396.972000  1638.776000   0.265463   0.734537  ...    21.0    1970 -241.804000        10.0          1             38.305000
    ## 4552          1970     NaN  1458.876000  1488.866000   0.550214   0.449786  ...    17.0    1970  -29.990000         9.0          1             20.389000
    ## 4553          1970     NaN  1386.799000  1436.731000   0.521671   0.478329  ...    25.0    1970  -49.932000       -15.0          0            -29.127000
    ## ...            ...     ...          ...          ...        ...        ...  ...     ...     ...         ...         ...        ...                   ...
    ## 16269         2018       d  1640.171960  1647.624483   0.582068   0.417932  ...    28.0    2010   -7.452523        13.0          1             21.496606
    ## 16270         2018       d  1669.105861  1633.114673   0.641378   0.358622  ...    14.0    2010   35.991188         6.0          1             13.344334
    ## 16271         2018       c  1682.450194  1648.424105   0.638772   0.361228  ...    26.0    2010   34.026089        -3.0          0            -18.545290
    ## 16272         2018       c  1675.286412  1661.668566   0.611248   0.388752  ...    37.0    2010   13.617846        -6.0          0            -24.670271
    ## 16273         2018       s  1666.969395  1686.338837   0.472154   0.527846  ...    13.0    2010  -19.369442       -10.0          0            -22.445895
    ## 
    ## [11725 rows x 19 columns]

    ## [Text(0, 0.5, 'difference in score'), Text(0.5, 0, 'difference in ELO'), Text(0.5, 1.0, 'Score vs pre-game ELO')]

<img src="/home/franklu/MDS/Workflows_Group_306/src/EDA_milestone2_files/figure-gfm/unnamed-chunk-2-1.png" width="672" />

    ## [Text(0, 0.5, 'difference in score'), Text(0.5, 0, 'change in elo after game'), Text(0.5, 1.0, 'Post-game ELO vs result')]

<img src="/home/franklu/MDS/Workflows_Group_306/src/EDA_milestone2_files/figure-gfm/unnamed-chunk-2-2.png" width="672" />

![](EDA_milestone2_files/figure-gfm/plot-1.png)<!-- -->
