
""" Runs classification model on the cleaned data to get the accuarcy on the test results

Usage: src/model.py --train_file=<train_file> --test_file=<test_file> 
Options:

--train_file=<train_file>    Training file
--test_file=<test_file>      Testing file

"""

import pandas as pd
import numpy as np
import altair as alt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from docopt import docopt
from sklearn.model_selection import GridSearchCV


opt = docopt(__doc__)

def main(train_file, test_file):

    X = train_file.drop(columns = 'status')
    y = train_file['status']
    X_test = test_file.drop(columns = 'status')
    y_test = test_file['status']
    
    parameters = {'max_depth':[2,4,6]}
    model = RandomForestClassifier()
    clf = GridSearchCV(model, parameters)
    clf.fit(X_train, y_train)    
    saveRDS(clf.score(X_test, y_test), file = "rf_score.rds")

    disp = plot_confusion_matrix(model, X_test, y_test,
                display_labels=['Non fraud', 'Fraud'],
                cmap=plt.cm.Reds, 
                values_format = 'd')

