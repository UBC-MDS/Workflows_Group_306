EDA
================

    ## sys.version_info(major=3, minor=7, micro=4, releaselevel='final', serial=0)

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

    ##             season playoff     elo1_pre  ...    elo2_post  score1  score2
    ## Unnamed: 0                               ...                             
    ## 0             1920     NaN  1503.947000  ...  1287.838000      48       0
    ## 1             1920     NaN  1493.002000  ...  1482.475000      14       0
    ## 2             1920     NaN  1516.108000  ...  1451.977000      45       0
    ## 3             1920     NaN  1368.333000  ...  1281.800000      20       0
    ## 4             1920     NaN  1504.688000  ...  1287.885000      48       0
    ## ...            ...     ...          ...  ...          ...     ...     ...
    ## 16536         2019       d  1694.572097  ...  1539.395070      51      31
    ## 16537         2019       d  1631.858399  ...  1567.848604      28      23
    ## 16538         2019       c  1707.523977  ...  1646.161779      35      24
    ## 16539         2019       c  1651.872498  ...  1621.187909      37      20
    ## 16540         2019       s  1723.941560  ...  1653.177962      31      20
    ## 
    ## [16541 rows x 8 columns]

## Correlation between columns

![](/mnt/doc/EDA/EDA_milestone3_files/figure-gfm/correlation%20heatmap-1.png)<!-- -->

## Because of the major rule change effective in 1970, remove data points before 1970

    ## /opt/conda/lib/python3.7/site-packages/pandas/core/indexing.py:844: SettingWithCopyWarning: 
    ## A value is trying to be set on a copy of a slice from a DataFrame.
    ## Try using .loc[row_indexer,col_indexer] = value instead
    ## 
    ## See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    ##   self.obj[key] = _infer_fill_value(value)
    ## /opt/conda/lib/python3.7/site-packages/pandas/core/indexing.py:964: SettingWithCopyWarning: 
    ## A value is trying to be set on a copy of a slice from a DataFrame.
    ## Try using .loc[row_indexer,col_indexer] = value instead
    ## 
    ## See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    ##   self.obj[item] = s

    ##    elo_vs_result  elo_vs_result.1
    ## 0  high_elo_lose             1686
    ## 1   high_elo_tie               28
    ## 2   high_elo_win             4193
    ## 3   low_elo_lose             3200
    ## 4    low_elo_tie               25
    ## 5    low_elo_win             2593

    ##             season playoff  ...  elo_change_aftergame  elo_vs_result
    ## Unnamed: 0                  ...                                     
    ## 4549          1970     NaN  ...             12.232000   high_elo_win
    ## 4550          1970     NaN  ...            -33.748000  high_elo_lose
    ## 4551          1970     NaN  ...             38.305000    low_elo_win
    ## 4552          1970     NaN  ...             20.389000    low_elo_win
    ## 4553          1970     NaN  ...            -29.127000   low_elo_lose
    ## ...            ...     ...  ...                   ...            ...
    ## 16269         2018       d  ...             21.496606    low_elo_win
    ## 16270         2018       d  ...             13.344334   high_elo_win
    ## 16271         2018       c  ...            -18.545290  high_elo_lose
    ## 16272         2018       c  ...            -24.670271  high_elo_lose
    ## 16273         2018       s  ...            -22.445895   low_elo_lose
    ## 
    ## [11725 rows x 14 columns]

## Plot for season games

    ## [Text(0, 0.5, 'difference in score'), Text(0.5, 0, 'difference in ELO'), Text(0.5, 1.0, 'Score vs pre-game ELO')]

![](/mnt/doc/EDA/EDA_milestone3_files/figure-gfm/plots-1.png)<!-- -->
![](/mnt/doc/EDA/EDA_milestone3_files/figure-gfm/plot-1.png)<!-- -->
