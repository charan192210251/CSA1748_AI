import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
data = pd.read_csv("sample.csv")
print(data.head())
data_encoded = pd.get_dummies(data)
X = data_encoded.iloc[:, :-1].values
y = data_encoded.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
plt.figure(figsize=(4,2))
plot_tree(clf, filled=True)
plt.show()
