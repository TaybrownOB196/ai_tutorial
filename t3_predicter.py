from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

import pandas as pd

df = pd.read_csv("C:\\Repo\\ai_tutorial\\tictactoe.csv")
columns = ["c0","c1","c2","c3","c4","c5","c6","c7","c8"]
# 0,0,0, 0,0,0, 0,0,0
sample_set = [[1,0,0, 1,-1,0, 0,-1,0]]
sample_df = pd.DataFrame(sample_set, columns=columns)

data = df[columns].copy()
y = df["label"].copy()

scaler = StandardScaler()
scaler.fit(data.values)

X_scaled = scaler.transform(data.values)

X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(X_scaled,
                                                                  y.values,
                                                             train_size=.9,
                                                           random_state=25)

logistic_regression = LogisticRegression()
svm = SVC()
tree = DecisionTreeClassifier()

logistic_regression.fit(X_train_scaled, y_train)
svm.fit(X_train_scaled, y_train)
tree.fit(X_train_scaled, y_train)

log_reg_preds = logistic_regression.predict(X_test_scaled)
svm_preds = svm.predict(X_test_scaled)
tree_preds = tree.predict(X_test_scaled)

sample = scaler.transform(sample_df.values)
print(logistic_regression.predict(sample))
print(svm.predict(sample))
print(tree.predict(sample))
