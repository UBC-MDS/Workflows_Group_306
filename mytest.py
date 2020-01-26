""" Runs classification model on the cleaned data to get the accuarcy on the test results

Usage: src/eda.py

"""
# --source=<source> --correlation=<correlation> --elo_win=<elo_win> --eda_score=<eda_score>
import numpy as np
import pandas as pd
import altair as alt
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import figure
# from numpy.polynomial.polynomial import polyfit
# import heatmap_func as hp
from docopt import docopt

opt = docopt(__doc__)

def main():

    source = pd.DataFrame({
        'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
    })

    pp = alt.Chart(source).mark_bar().encode(
        x='a',
        y='b'
    )
    pp.save('my_test.png')

if __name__ == "__main__":
    main()
