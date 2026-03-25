import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle

data = pd.read_csv("Week9/titanic_new.csv")

X = data.drop(["Survived"], axis=1)
y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


dt = DecisionTreeClassifier()
dt_model = dt.fit(X_train, y_train)

dt_pred = dt_model.predict(X_test)

#with open("Week10/titanic_model.pkl", "wb") as file:
#    pickle.dump(dt_model, file)

with open("Week10/titanic_model.pkl", "rb") as file:
    t_model = pickle.load(file)

values = [[2, 1, 29, 0, 1, 16.0]]
new_df = pd.DataFrame(values, columns=["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"])
dt_pred = t_model.predict(new_df)
print(dt_pred)