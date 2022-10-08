import pandas as pd
import numpy as np
import pickle
from utils import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from config import MODEL_PATH

# if pkl file cannot file create the model
print('Training Started...')
data = datasets.loadDataSet()
X = data.data
Y = data.target
X_train, X_test, y_train, y_test = train_test_split(X,Y, random_state = 50, test_size = 0.25)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
with open(MODEL_PATH, 'wb') as f:
    pickle.dump(clf, f)
print('Training Completed !')