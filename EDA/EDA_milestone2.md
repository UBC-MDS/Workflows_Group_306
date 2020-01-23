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

    ##                   season   neutral  elo1_pre  ...  qbelo2_post    score1    score2
    ## season          1.000000  0.052257  0.065014  ...     0.056153  0.187462  0.243275
    ## neutral         0.052257  1.000000  0.079682  ...     0.077180  0.014754  0.018024
    ## elo1_pre        0.065014  0.079682  1.000000  ...     0.069377  0.222497 -0.181046
    ## elo2_pre        0.104371  0.076470  0.084598  ...     0.965843 -0.168403  0.219393
    ## elo_prob1      -0.025237 -0.032878  0.673498  ...    -0.649803  0.285565 -0.295814
    ## elo_prob2       0.025237  0.032878 -0.673498  ...     0.649803 -0.285565  0.295814
    ## elo1_post       0.061251  0.079616  0.979733  ...     0.025535  0.327687 -0.290680
    ## elo2_post       0.103981  0.073102  0.078909  ...     0.989821 -0.276433  0.329864
    ## qbelo1_pre      0.058135  0.086485  0.989067  ...     0.067809  0.217140 -0.191650
    ## qbelo2_pre      0.058914  0.080422  0.072723  ...     0.976796 -0.174151  0.197877
    ## qb1_value_pre   0.426907  0.066528  0.480057  ...     0.040765  0.216789 -0.018213
    ## qb2_value_pre   0.428205  0.064206  0.036567  ...     0.434261 -0.022974  0.216750
    ## qb1_adj         0.030593  0.029570  0.136279  ...     0.034289  0.096727 -0.038061
    ## qb2_adj         0.032736  0.012128  0.016654  ...     0.089500 -0.023213  0.078036
    ## qbelo_prob1     0.004626 -0.025006  0.663970  ...    -0.625622  0.292288 -0.291270
    ## qbelo_prob2    -0.004626  0.025006 -0.663970  ...     0.625622 -0.292288  0.291270
    ## qb1_game_value  0.163155  0.032562  0.191296  ...    -0.104724  0.602309 -0.056518
    ## qb2_game_value  0.150389  0.022739 -0.048178  ...     0.249927 -0.072474  0.610369
    ## qb1_value_post  0.419918  0.067180  0.474026  ...     0.011914  0.335103 -0.029540
    ## qb2_value_post  0.419156  0.062939  0.021303  ...     0.447938 -0.037503  0.336721
    ## qbelo1_post     0.058182  0.085858  0.966975  ...     0.022174  0.333033 -0.310853
    ## qbelo2_post     0.056153  0.077180  0.069377  ...     1.000000 -0.293211  0.319151
    ## score1          0.187462  0.014754  0.222497  ...    -0.293211  1.000000  0.018748
    ## score2          0.243275  0.018024 -0.181046  ...     0.319151  0.018748  1.000000
    ## 
    ## [24 rows x 24 columns]

## Because of the major rule change effective in 1970, remove data points before 1970

    ##             season playoff     elo1_pre  ...  score1  score2  decade
    ## Unnamed: 0                               ...                        
    ## 4549          1970     NaN  1583.202000  ...    34.0    13.0    1970
    ## 4550          1970     NaN  1475.119000  ...    16.0    24.0    1970
    ## 4551          1970     NaN  1396.972000  ...    31.0    21.0    1970
    ## 4552          1970     NaN  1458.876000  ...    26.0    17.0    1970
    ## 4553          1970     NaN  1386.799000  ...    10.0    25.0    1970
    ## ...            ...     ...          ...  ...     ...     ...     ...
    ## 16269         2018       d  1640.171960  ...    41.0    28.0    2010
    ## 16270         2018       d  1669.105861  ...    20.0    14.0    2010
    ## 16271         2018       c  1682.450194  ...    23.0    26.0    2010
    ## 16272         2018       c  1675.286412  ...    31.0    37.0    2010
    ## 16273         2018       s  1666.969395  ...     3.0    13.0    2010
    ## 
    ## [11725 rows x 15 columns]

## Plot for season games

    ## /home/franklu/anaconda3/bin/python:1: SettingWithCopyWarning: 
    ## A value is trying to be set on a copy of a slice from a DataFrame.
    ## Try using .loc[row_indexer,col_indexer] = value instead
    ## 
    ## See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

    ##             season playoff  ...  is_winner  elo_change_aftergame
    ## Unnamed: 0                  ...                                 
    ## 4549          1970     NaN  ...          1             12.232000
    ## 4550          1970     NaN  ...          0            -33.748000
    ## 4551          1970     NaN  ...          1             38.305000
    ## 4552          1970     NaN  ...          1             20.389000
    ## 4553          1970     NaN  ...          0            -29.127000
    ## ...            ...     ...  ...        ...                   ...
    ## 16258         2018     NaN  ...          1              2.948560
    ## 16259         2018     NaN  ...          0            -30.964753
    ## 16260         2018     NaN  ...          0            -18.639829
    ## 16261         2018     NaN  ...          1              7.048405
    ## 16262         2018     NaN  ...          0            -36.685177
    ## 
    ## [11236 rows x 19 columns]

    ## [Text(0, 0.5, 'difference in score'), Text(0.5, 0, 'difference in ELO'), Text(0.5, 1.0, 'Score vs pre-game ELO')]

<img src="/home/franklu/MDS/Workflows_Group_306/EDA/EDA_milestone2_files/figure-gfm/unnamed-chunk-4-1.png" width="672" />

    ## [Text(0, 0.5, 'difference in score'), Text(0.5, 0, 'change in elo after game'), Text(0.5, 1.0, 'Post-game ELO vs result')]

<img src="/home/franklu/MDS/Workflows_Group_306/EDA/EDA_milestone2_files/figure-gfm/unnamed-chunk-4-2.png" width="672" />

![](EDA_milestone2_files/figure-gfm/plot-1.png)<!-- -->
