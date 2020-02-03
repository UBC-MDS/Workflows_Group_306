
#author : Simardeep Kaur
#date : 25 January, 2020

""" Runs classification model on the cleaned data to get the accuarcy on the test results

Usage: src/model.py --train_file=<train_file> --test_file=<test_file>

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
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt



opt = docopt(__doc__)

def main(train_file, test_file):



    data = pd.read_csv(train_file)
    test_data =  pd.read_csv(test_file)

    try:
      data.to_csv(train_file, index = False)
    except:
      os.makedirs(os.path.dirname(train_file))
      data.to_csv(train_file, index = False)



    X = data.drop(columns = 'status')
    y = data['status']
    X_test = test_data.drop(columns = 'status')
    y_test = test_data['status']

    ## Checking whether X_test has training examples
    try:
        X_test.shape[0] == 0 and X.shape[0]
    except:
        print("Please check the data")


    #Random forest Classification
    parameters = {'max_depth':[2,4,6]}
    model = RandomForestClassifier()
    clf = GridSearchCV(model, parameters, cv = 5)
    clf.fit(X, y)
    rf_score = clf.score(X_test, y_test)
    rf_data =  pd.DataFrame({'rf_score':[round(rf_score, 3)]})
    rf_data.to_csv(path_or_buf='data/rf_score.csv', index = False)


    #Logistic Regression
    lr_model = LogisticRegression(solver = 'liblinear')
    lr_model.fit(X, y)
    lr_Score = lr_model.score(X_test, y_test)
    lr_data =  pd.DataFrame({'lr_score':[round(lr_Score, 3)]})
    lr_data.to_csv(path_or_buf='data/lr_score.csv', index = False)



    disp = plot_confusion_matrix(clf, X_test, y_test,
                cmap=plt.cm.Reds,
                values_format = 'd')
    plt.savefig('img/disp_rf.png')

    disp = plot_confusion_matrix(lr_model, X_test, y_test,
                cmap=plt.cm.Reds,
                values_format = 'd')
    plt.savefig('img/disp_lr.png')


if __name__ == "__main__":
    main(opt["--train_file"],opt["--test_file"])
