import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Support vector machine classification of experienced/inexperienced debaters.

# Kernel used: linear.

# Features used: (FP1, FP2, F4) * (alpha, beta, theta)
# (predicted by literature).

# Read dataset to pandas dataframe.
beginners = pd.read_csv("/home/merkel/Downloads/fd_beginners", index_col = 0)

# drop NaN values
beginners = beginners.dropna(axis = 0)

# save all anger moments
anger = beginners.loc[beginners['anger'] == 1]
print(anger.shape)

# save all non-anger momnets
nonanger = beginners.loc[beginners['anger'] == 0]

# sample 1217 rows (number of anger moments)
nonanger_sample = nonanger.sample(n = 1217)
print(nonanger_sample.shape)

data =  pd.concat([anger, nonanger_sample], axis = 0)
print(data)
print(data.shape)

# Save everything but anger class.
x = data[['alpha 1', 'beta 1', 'theta 1', 'alpha 2', 'beta 2', 'theta 2', 'alpha 4', 'beta 4', 'theta 4', 'alpha 6', 'beta 6', 'theta 6', 'alpha 16', 'beta 16', 'theta 16']];

print(x)

# Save only anger class.
y = data['anger']

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()

from sklearn.model_selection import GridSearchCV
# create a dictionary of all values we want to test for n_neighbors
param_grid = {'n_neighbors': np.arange(1, 25)}

# use gridsearch to test all values for n_neighbors
knn_gscv = GridSearchCV(knn, param_grid, cv=10)

# fit model to data
knn_gscv.fit(x, y)

# check top performing n_neighbors value
print(knn_gscv.best_params_)

# save best k to use for classification
kNeighbors = knn_gscv.best_params_.get('n_neighbors')

# construct new knn with optimal neighbors
knn = KNeighborsClassifier(kNeighbors)

# Perform K-fold cross-validation with 10 folds.
from sklearn.model_selection import cross_val_score
scores = cross_val_score(knn, x, y, cv = 150)

# Print accuracy scores.
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))