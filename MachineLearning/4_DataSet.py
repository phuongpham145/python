from sklearn.datasets import load_iris
# 75% trainning con lai kiem tra
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.tree import DecisionTreeClassifier
iris_dataset = load_iris()
# print(iris_dataset.data)
# print(iris_dataset.target)
X_train, X_text, Y_train, Y_text = train_test_split(
    iris_dataset.data, iris_dataset.target, random_state=0) #Dang numpy
print(X_train)
print(Y_text)
model = DecisionTreeClassifier()
mymodel = model.fit(X_train, Y_train)
X_new = np.array([[6.0, 3.23, 4.5, 2.0]])
print(mymodel.predict(X_text))
print(mymodel.predict(X_new))
print(mymodel.score(X_text, Y_text))
