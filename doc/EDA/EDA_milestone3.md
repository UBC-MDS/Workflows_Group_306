EDA
================

## The information about columns

    ## <class 'pandas.core.frame.DataFrame'>
    ## Int64Index: 16541 entries, 0 to 16540
    ## Data columns (total 30 columns):
    ##  #   Column          Non-Null Count  Dtype  
    ## ---  ------          --------------  -----  
    ##  0   date            16541 non-null  object 
    ##  1   season          16541 non-null  int64  
    ##  2   neutral         16541 non-null  int64  
    ##  3   playoff         577 non-null    object 
    ##  4   team1           16541 non-null  object 
    ##  5   team2           16541 non-null  object 
    ##  6   elo1_pre        16541 non-null  float64
    ##  7   elo2_pre        16541 non-null  float64
    ##  8   elo_prob1       16541 non-null  float64
    ##  9   elo_prob2       16541 non-null  float64
    ##  10  elo1_post       16541 non-null  float64
    ##  11  elo2_post       16541 non-null  float64
    ##  12  qbelo1_pre      14379 non-null  float64
    ##  13  qbelo2_pre      14379 non-null  float64
    ##  14  qb1             14379 non-null  object 
    ##  15  qb2             14379 non-null  object 
    ##  16  qb1_value_pre   14379 non-null  float64
    ##  17  qb2_value_pre   14379 non-null  float64
    ##  18  qb1_adj         14379 non-null  float64
    ##  19  qb2_adj         14379 non-null  float64
    ##  20  qbelo_prob1     14379 non-null  float64
    ##  21  qbelo_prob2     14379 non-null  float64
    ##  22  qb1_game_value  14379 non-null  float64
    ##  23  qb2_game_value  14379 non-null  float64
    ##  24  qb1_value_post  14379 non-null  float64
    ##  25  qb2_value_post  14379 non-null  float64
    ##  26  qbelo1_post     14379 non-null  float64
    ##  27  qbelo2_post     14379 non-null  float64
    ##  28  score1          16541 non-null  int64  
    ##  29  score2          16541 non-null  int64  
    ## dtypes: float64(20), int64(4), object(6)
    ## memory usage: 3.9+ MB

    ##             season playoff     elo1_pre     elo2_pre    elo1_post    elo2_post  score1  score2
    ## Unnamed: 0                                                                                    
    ## 0             1920     NaN  1503.947000  1300.000000  1516.108000  1287.838000      48       0
    ## 1             1920     NaN  1493.002000  1504.908000  1515.434000  1482.475000      14       0
    ## 2             1920     NaN  1516.108000  1478.004000  1542.135000  1451.977000      45       0
    ## 3             1920     NaN  1368.333000  1300.000000  1386.533000  1281.800000      20       0
    ## 4             1920     NaN  1504.688000  1300.000000  1516.803000  1287.885000      48       0
    ## ...            ...     ...          ...          ...          ...          ...     ...     ...
    ## 16536         2019       d  1694.572097  1552.346950  1707.523977  1539.395070      51      31
    ## 16537         2019       d  1631.858399  1579.312894  1643.322690  1567.848604      28      23
    ## 16538         2019       c  1707.523977  1662.579362  1723.941560  1646.161779      35      24
    ## 16539         2019       c  1651.872498  1643.322690  1674.007279  1621.187909      37      20
    ## 16540         2019       s  1723.941560  1674.007279  1744.770876  1653.177962      31      20
    ## 
    ## [16541 rows x 8 columns]

## Correlation between columns

<img src="/home/franklu/MDS/Workflows_Group_306/doc/EDA/EDA_milestone3_files/figure-gfm/correlation heatmap-1.png" width="672" />

## Because of the major rule change effective in 1970, remove data points before 1970

    ## /home/franklu/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py:844: SettingWithCopyWarning: 
    ## A value is trying to be set on a copy of a slice from a DataFrame.
    ## Try using .loc[row_indexer,col_indexer] = value instead
    ## 
    ## See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    ##   self.obj[key] = _infer_fill_value(value)
    ## /home/franklu/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py:964: SettingWithCopyWarning: 
    ## A value is trying to be set on a copy of a slice from a DataFrame.
    ## Try using .loc[row_indexer,col_indexer] = value instead
    ## 
    ## See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    ##   self.obj[item] = s

    ##             season playoff     elo1_pre     elo2_pre    elo1_post    elo2_post  ...  decade    elo_diff  score_diff  is_winner  elo_change_aftergame  elo_vs_result
    ## Unnamed: 0                                                                      ...                                                                                
    ## 4549          1970     NaN  1583.202000  1426.127000  1595.434000  1413.895000  ...    1970  157.075000          21          1             12.232000   high_elo_win
    ## 4550          1970     NaN  1475.119000  1382.173000  1441.371000  1415.921000  ...    1970   92.946000          -8          0            -33.748000  high_elo_lose
    ## 4551          1970     NaN  1396.972000  1638.776000  1435.277000  1600.471000  ...    1970 -241.804000          10          1             38.305000    low_elo_win
    ## 4552          1970     NaN  1458.876000  1488.866000  1479.265000  1468.477000  ...    1970  -29.990000           9          1             20.389000    low_elo_win
    ## 4553          1970     NaN  1386.799000  1436.731000  1357.672000  1465.858000  ...    1970  -49.932000         -15          0            -29.127000   low_elo_lose
    ## ...            ...     ...          ...          ...          ...          ...  ...     ...         ...         ...        ...                   ...            ...
    ## 16269         2018       d  1640.171960  1647.624483  1661.668566  1626.127877  ...    2010   -7.452523          13          1             21.496606    low_elo_win
    ## 16270         2018       d  1669.105861  1633.114673  1682.450194  1619.770339  ...    2010   35.991188           6          1             13.344334   high_elo_win
    ## 16271         2018       c  1682.450194  1648.424105  1663.904905  1666.969395  ...    2010   34.026089          -3          0            -18.545290  high_elo_lose
    ## 16272         2018       c  1675.286412  1661.668566  1650.616141  1686.338837  ...    2010   13.617846          -6          0            -24.670271  high_elo_lose
    ## 16273         2018       s  1666.969395  1686.338837  1644.523499  1708.784732  ...    2010  -19.369442         -10          0            -22.445895   low_elo_lose
    ## 
    ## [11725 rows x 14 columns]

## Plot for season games

    ## [Text(0, 0.5, 'difference in score'), Text(0.5, 0, 'difference in ELO'), Text(0.5, 1.0, 'Score vs pre-game ELO')]

<img src="/home/franklu/MDS/Workflows_Group_306/doc/EDA/EDA_milestone3_files/figure-gfm/plots-1.png" width="672" />
![](/home/franklu/MDS/Workflows_Group_306/doc/EDA/EDA_milestone3_files/figure-gfm/plot-1.png)<!-- -->
