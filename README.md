# Workflows_Group_306

Project Proposal

The website [FiveThirtyEight](https://fivfethirtyeight.com/) launched a [“prediction game”](https://fivethirtyeight.com/features/how-to-play-our-nfl-predictions-game/) for NFL games this year, in which the readers assign a probability to to each teams wining chances for every game, competing with fivethirtyeight’s ELO based prediction system.

ELO ranking is a relative ranking system in which performing better then what the ELO would predict leads to an increase in ranking and performing worse that would be expected leads to  decrees. Where predictions and expectations are based on the difference between two players/teams ELO ratings.

A more general explanation can be found [here](https://www.youtube.com/watch?v=AsYfbmp0To0) by Singingbanana on youtube.

In order to test whether or not ELO is a valid method by which to predict NFL game outcomes, a sport which has coined the saying “any given Sunday”, we will attempt to use historic ELO ratings to predict the winners of the 2019-2020 season games which has recently ended.
We will attempt to do so using ML classification algorithems such as logistic regression, random forest, and others.

The data for this project will be the same data fivethirtyeigh uses to generate their own predictions which can be found in [this](https://github.com/fivethirtyeight/data/tree/master/nfl-elo) github repo.

We will be focusing on the years following the 1970 AFL and NFL merger, which roughly shaped the NFL as we know it today.


The following table shows average statistics of the elo grades by decade for winning vs losing team:

![](https://github.com/TBarasch/Workflows_Group_306/blob/master/img/table.png?raw=true)


In addition the following graph shows that although it may seem a little low, there appears to some correlation between the difference in ELO score and the outcome

![](https://github.com/TBarasch/Workflows_Group_306/blob/master/img/score_vs_elo.png?raw=true)

And finally the following graph shows how a teams ELO score changes in relation to the final score diff in points

![](https://github.com/TBarasch/Workflows_Group_306/blob/master/img/cropped.png?raw=true)

Which unsuprisingly usually decreeses for the losing team, and increases for the winnning team.
