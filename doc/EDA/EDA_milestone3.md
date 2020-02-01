EDA
================

## The information about columns

    ## <class 'pandas.core.frame.DataFrame'>
    ## Int64Index: 16541 entries, 0 to 16540
    ## Data columns (total 30 columns):
    ## date              16541 non-null object
    ## season            16541 non-null int64
    ## neutral           16541 non-null int64
    ## playoff           577 non-null object
    ## team1             16541 non-null object
    ## team2             16541 non-null object
    ## elo1_pre          16541 non-null float64
    ## elo2_pre          16541 non-null float64
    ## elo_prob1         16541 non-null float64
    ## elo_prob2         16541 non-null float64
    ## elo1_post         16540 non-null float64
    ## elo2_post         16540 non-null float64
    ## qbelo1_pre        14378 non-null float64
    ## qbelo2_pre        14378 non-null float64
    ## qb1               14379 non-null object
    ## qb2               14379 non-null object
    ## qb1_value_pre     14379 non-null float64
    ## qb2_value_pre     14379 non-null float64
    ## qb1_adj           14379 non-null float64
    ## qb2_adj           14379 non-null float64
    ## qbelo_prob1       14379 non-null float64
    ## qbelo_prob2       14379 non-null float64
    ## qb1_game_value    14378 non-null float64
    ## qb2_game_value    14378 non-null float64
    ## qb1_value_post    14378 non-null float64
    ## qb2_value_post    14378 non-null float64
    ## qbelo1_post       14378 non-null float64
    ## qbelo2_post       14378 non-null float64
    ## score1            16540 non-null float64
    ## score2            16540 non-null float64
    ## dtypes: float64(22), int64(2), object(6)
    ## memory usage: 3.9+ MB

    ##             season playoff     elo1_pre     elo2_pre    elo1_post    elo2_post  score1  score2
    ## Unnamed: 0                                                                                    
    ## 0             1920     NaN  1503.947000  1300.000000  1516.108000  1287.838000    48.0     0.0
    ## 1             1920     NaN  1493.002000  1504.908000  1515.434000  1482.475000    14.0     0.0
    ## 2             1920     NaN  1516.108000  1478.004000  1542.135000  1451.977000    45.0     0.0
    ## 3             1920     NaN  1368.333000  1300.000000  1386.533000  1281.800000    20.0     0.0
    ## 4             1920     NaN  1504.688000  1300.000000  1516.803000  1287.885000    48.0     0.0
    ## ...            ...     ...          ...          ...          ...          ...     ...     ...
    ## 16536         2019       d  1694.572097  1552.346950  1707.523977  1539.395070    51.0    31.0
    ## 16537         2019       d  1631.858399  1579.312894  1643.322690  1567.848604    28.0    23.0
    ## 16538         2019       c  1707.523977  1662.579362  1723.941560  1646.161779    35.0    24.0
    ## 16539         2019       c  1651.872498  1643.322690  1674.007279  1621.187909    37.0    20.0
    ## 16540         2019       s  1723.941560  1674.007279          NaN          NaN     NaN     NaN
    ## 
    ## [16541 rows x 8 columns]

## Correlation between columns

<img src="/home/franklu/MDS/Workflows_Group_306/doc/EDA/EDA_milestone3_files/figure-gfm/correlation heatmap-1.png" width="672" />

## Because of the major rule change effective in 1970, remove data points before 1970

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

    ##             season playoff     elo1_pre     elo2_pre    elo1_post  ...    elo_diff  score_diff  is_winner  elo_change_aftergame  elo_vs_result
    ## Unnamed: 0                                                         ...                                                                        
    ## 4549          1970     NaN  1583.202000  1426.127000  1595.434000  ...  157.075000        21.0          1             12.232000   high_elo_win
    ## 4550          1970     NaN  1475.119000  1382.173000  1441.371000  ...   92.946000        -8.0          0            -33.748000  high_elo_lose
    ## 4551          1970     NaN  1396.972000  1638.776000  1435.277000  ... -241.804000        10.0          1             38.305000    low_elo_win
    ## 4552          1970     NaN  1458.876000  1488.866000  1479.265000  ...  -29.990000         9.0          1             20.389000    low_elo_win
    ## 4553          1970     NaN  1386.799000  1436.731000  1357.672000  ...  -49.932000       -15.0          0            -29.127000   low_elo_lose
    ## ...            ...     ...          ...          ...          ...  ...         ...         ...        ...                   ...            ...
    ## 16269         2018       d  1640.171960  1647.624483  1661.668566  ...   -7.452523        13.0          1             21.496606    low_elo_win
    ## 16270         2018       d  1669.105861  1633.114673  1682.450194  ...   35.991188         6.0          1             13.344334   high_elo_win
    ## 16271         2018       c  1682.450194  1648.424105  1663.904905  ...   34.026089        -3.0          0            -18.545290  high_elo_lose
    ## 16272         2018       c  1675.286412  1661.668566  1650.616141  ...   13.617846        -6.0          0            -24.670271  high_elo_lose
    ## 16273         2018       s  1666.969395  1686.338837  1644.523499  ...  -19.369442       -10.0          0            -22.445895   low_elo_lose
    ## 
    ## [11725 rows x 14 columns]

## Plot for season games

    ## [Text(0, 0.5, 'difference in score'), Text(0.5, 0, 'difference in ELO'), Text(0.5, 1.0, 'Score vs pre-game ELO')]

<img src="/home/franklu/MDS/Workflows_Group_306/doc/EDA/EDA_milestone3_files/figure-gfm/plots-1.png" width="672" />
![](/home/franklu/MDS/Workflows_Group_306/doc/EDA/EDA_milestone3_files/figure-gfm/plot-1.png)<!-- -->
