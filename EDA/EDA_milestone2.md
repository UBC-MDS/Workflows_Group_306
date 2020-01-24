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

<img src="/home/franklu/MDS/Workflows_Group_306/EDA/EDA_milestone2_files/figure-gfm/unnamed-chunk-2-1.png" width="672" />

## Because of the major rule change effective in 1970, remove data points before 1970

    ##             season playoff     elo1_pre     elo2_pre  elo_prob1  elo_prob2    elo1_post    elo2_post   qbelo1_pre   qbelo2_pre  qbelo_prob1  qbelo_prob2  score1  score2  decade
    ## Unnamed: 0                                                                                                                                                                      
    ## 4549          1970     NaN  1583.202000  1426.127000   0.782172   0.217828  1595.434000  1413.895000  1575.663197  1419.063694     0.787242     0.212758    34.0    13.0    1970
    ## 4550          1970     NaN  1475.119000  1382.173000   0.712839   0.287161  1441.371000  1415.921000  1468.322928  1392.110372     0.702241     0.297759    16.0    24.0    1970
    ## 4551          1970     NaN  1396.972000  1638.776000   0.265463   0.734537  1435.277000  1600.471000  1395.779057  1634.838107     0.260615     0.739385    31.0    21.0    1970
    ## 4552          1970     NaN  1458.876000  1488.866000   0.550214   0.449786  1479.265000  1468.477000  1462.726939  1484.068018     0.562264     0.437736    26.0    17.0    1970
    ## 4553          1970     NaN  1386.799000  1436.731000   0.521671   0.478329  1357.672000  1465.858000  1369.469608  1428.578167     0.496323     0.503677    10.0    25.0    1970
    ## ...            ...     ...          ...          ...        ...        ...          ...          ...          ...          ...          ...          ...     ...     ...     ...
    ## 16269         2018       d  1640.171960  1647.624483   0.582068   0.417932  1661.668566  1626.127877  1639.987545  1638.343453     0.674251     0.325749    41.0    28.0    2010
    ## 16270         2018       d  1669.105861  1633.114673   0.641378   0.358622  1682.450194  1619.770339  1648.918757  1609.607539     0.717901     0.282099    20.0    14.0    2010
    ## 16271         2018       c  1682.450194  1648.424105   0.638772   0.361228  1663.904905  1666.969395  1659.143400  1639.538714     0.634698     0.365302    23.0    26.0    2010
    ## 16272         2018       c  1675.286412  1661.668566   0.611248   0.388752  1650.616141  1686.338837  1643.881166  1656.246942     0.615809     0.384191    31.0    37.0    2010
    ## 16273         2018       s  1666.969395  1686.338837   0.472154   0.527846  1644.523499  1708.784732  1657.938921  1681.140535     0.460387     0.539613     3.0    13.0    2010
    ## 
    ## [11725 rows x 15 columns]

## Plot for season games

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

    ##             season playoff     elo1_pre     elo2_pre  elo_prob1  elo_prob2    elo1_post    elo2_post  ...  qbelo_prob2  score1  score2  decade    elo_diff  score_diff  is_winner  elo_change_aftergame
    ## Unnamed: 0                                                                                            ...                                                                                              
    ## 4549          1970     NaN  1583.202000  1426.127000   0.782172   0.217828  1595.434000  1413.895000  ...     0.212758    34.0    13.0    1970  157.075000        21.0          1             12.232000
    ## 4550          1970     NaN  1475.119000  1382.173000   0.712839   0.287161  1441.371000  1415.921000  ...     0.297759    16.0    24.0    1970   92.946000        -8.0          0            -33.748000
    ## 4551          1970     NaN  1396.972000  1638.776000   0.265463   0.734537  1435.277000  1600.471000  ...     0.739385    31.0    21.0    1970 -241.804000        10.0          1             38.305000
    ## 4552          1970     NaN  1458.876000  1488.866000   0.550214   0.449786  1479.265000  1468.477000  ...     0.437736    26.0    17.0    1970  -29.990000         9.0          1             20.389000
    ## 4553          1970     NaN  1386.799000  1436.731000   0.521671   0.478329  1357.672000  1465.858000  ...     0.503677    10.0    25.0    1970  -49.932000       -15.0          0            -29.127000
    ## ...            ...     ...          ...          ...        ...        ...          ...          ...  ...          ...     ...     ...     ...         ...         ...        ...                   ...
    ## 16258         2018     NaN  1602.533070  1326.059193   0.877147   0.122853  1605.481630  1323.110633  ...     0.103203    27.0    24.0    2010  276.473877         3.0          1              2.948560
    ## 16259         2018     NaN  1586.100685  1608.712110   0.560701   0.439299  1555.135931  1639.676863  ...     0.501900    10.0    24.0    2010  -22.611425       -14.0          0            -30.964753
    ## 16260         2018     NaN  1439.886121  1604.977617   0.359814   0.640186  1421.246292  1623.617446  ...     0.651388     9.0    23.0    2010 -165.091495       -14.0          0            -18.639829
    ## 16261         2018     NaN  1649.009776  1362.709331   0.883113   0.116887  1656.058181  1355.660927  ...     0.103887    35.0     3.0    2010  286.300445        32.0          1              7.048405
    ## 16262         2018     NaN  1562.545982  1541.055633   0.621961   0.378039  1525.860805  1577.740810  ...     0.485187    17.0    33.0    2010   21.490349       -16.0          0            -36.685177
    ## 
    ## [11236 rows x 19 columns]

    ## [Text(0, 0.5, 'difference in score'), Text(0.5, 0, 'difference in ELO'), Text(0.5, 1.0, 'Score vs pre-game ELO')]

<img src="/home/franklu/MDS/Workflows_Group_306/EDA/EDA_milestone2_files/figure-gfm/unnamed-chunk-4-1.png" width="672" />

    ## [Text(0, 0.5, 'difference in score'), Text(0.5, 0, 'change in elo after game'), Text(0.5, 1.0, 'Post-game ELO vs result')]

<img src="/home/franklu/MDS/Workflows_Group_306/EDA/EDA_milestone2_files/figure-gfm/unnamed-chunk-4-2.png" width="672" />

![](EDA_milestone2_files/figure-gfm/plot-1.png)<!-- -->
