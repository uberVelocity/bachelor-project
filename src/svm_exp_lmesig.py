import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Support vector machine classification of experienced debaters.

# Kernel used: radial basis function

# Features used: (FP1, FP2, F7, F4, T8, CP6, P4) * (alpha, beta, theta)
# (found significant by Linear-Mixed-Effects model).

# Read dataset to pandas dataframe.
experienced = pd.read_csv("/home/merkel/Downloads/fd_experienced", index_col = 0)

# drop NaN values
experienced = experienced.dropna(axis = 0)

# save all anger moments
anger = experienced.loc[experienced['anger'] == 1]
print(anger.shape)

# save all non-anger momnets
nonanger = experienced.loc[experienced['anger'] == 0]

# sample 1217 rows (number of anger moments)
nonanger_sample = nonanger.sample(n = 1217)
print(nonanger_sample.shape)

data =  pd.concat([anger, nonanger_sample], axis = 0)
print(data)
print(data.shape)

# Save everything but anger class.
x = data[['alpha 1', 'beta 1', 'theta 1', 'alpha 2', 'beta 2', 'theta 2', 'alpha 3', 'theta 3', 'alpha 6', 'beta 6', 'theta 6', 'alpha 21', 'beta 21', 'theta 21', 'alpha 16', 'beta 16', 'theta 16', 'alpha 26', 'beta 26', 'theta 26']];

print(x)

# Save only anger class.
y = data['anger']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

from sklearn.svm import SVC

svclassifier = SVC(kernel = 'rbf')
svclassifier.fit(x_train, y_train)

y_pred = svclassifier.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))    