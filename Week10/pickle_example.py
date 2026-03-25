import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle
from sklearn.model_selection import GridSearchCV, KFold

data = pd.read_csv("Week9/titanic_new.csv")

X = data.drop(["Survived"], axis=1)
y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


dt = DecisionTreeClassifier()

# get the best model
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
best_model = grid_search.best_estimator_


#save best model
#with open("Week10/titanic_model.pkl", "wb") as file:
#    pickle.dump(best_model, file)

#load
with open("Week10/titanic_model.pkl", "rb") as file:
    t_model = pickle.load(file)

values = [[2, 1, 29, 0, 1, 16.0]]
new_df = pd.DataFrame(values, columns=["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"])
dt_pred = t_model.predict(new_df)
print(dt_pred)