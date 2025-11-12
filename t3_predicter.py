from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

import os
import pandas as pd
from dotenv import load_dotenv
import joblib

load_dotenv()
columns = ["c0","c1","c2","c3","c4","c5","c6","c7","c8"]
scaler = StandardScaler()
logistic_regression = LogisticRegression()
svm = SVC()
tree = DecisionTreeClassifier()

def train_model():
    csv_path = os.getenv("T3_DATA_FILE_PATH")

    df = pd.read_csv(csv_path)
    # 0,0,0, 0,0,0, 0,0,0

    data = df[columns].copy()
    y = df["label"].copy()

    scaler.fit(data.values)

    X_scaled = scaler.transform(data.values)

    X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(X_scaled, y.values, train_size=.7, random_state=25)

    logistic_regression.fit(X_train_scaled, y_train)
    svm.fit(X_train_scaled, y_train)
    tree.fit(X_train_scaled, y_train)

def predict(sample_set: list[list[int]]):
    # sample_set = [[1,0,0, 0,0,0, 1,0,-1]]
    sample_df = pd.DataFrame(sample_set, columns=columns)
    sample = scaler.transform(sample_df.values)

    print(logistic_regression.predict(sample))
    print(svm.predict(sample))
    print(tree.predict(sample))

def save_model(filename: str):
    joblib.dump(tree, filename)

def load_model(filename: str):
    return joblib.load(filename)

# if __name__ == '__main__':
#     sample_set = [[1,0,0, 0,0,0, 1,0,-1]]
#     train_model()
#     predict(sample_set)
#     save_model('ttt.model')

sample_set = [[1,0,0, 0,0,0, 1,0,-1]]
loaded_model = load_model('ttt.model')
print(loaded_model.predict(sample_set))