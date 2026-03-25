import pandas as pd
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("Week7/iris.csv")

X = data.drop(["species"], axis=1)
y = data["species"]

dt = DecisionTreeClassifier()

# Hyperparameters and the values to try
param_grid = {
    'max_depth': [None, 2, 4, 6],
    'min_samples_split': [2, 5, 10],
}

# KFold cross validation with 5 folds
kf = KFold(n_splits=5, shuffle=True)

# Create your grid search and train the models
grid_search = GridSearchCV(dt, param_grid, cv=kf, scoring="accuracy")
grid_search.fit(X, y)

# Store the best performing model
best_model = grid_search.best_estimator_

print(grid_search.best_params_)
print(grid_search.best_score_)

# More in-depth breakdown of each fold/training session
# print(grid_search.cv_results_)
