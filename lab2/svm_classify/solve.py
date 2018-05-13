# -*- coding:utf-8 -*- #
from sklearn import datasets
from sklearn.model_selection import train_test_split
# add package here
from sklearn.svm import SVC

iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target
# 利用x_train y_train作为训练集
x_train, x_test, y_train, y_test = train_test_split(iris_x, iris_y, test_size=0.3)


class Solution():
    def solve(self, test_data):
        # call function classification
        svc = SVC()
        svc.fit(x_train,y_train)
        return svc.predict(test_data)
        pass
