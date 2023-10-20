import numpy as np


class preceptron:
    def __init__(self, learn, theta=None):
        self.theta = theta
        self.learn = learn

    def train_learn(self, X, Y):
        # theta是一个n+1*1的列向量，最后一行代表常数项
        self.theta=np.matrix(np.zeros(X.shape[1]+1).reshape(-1,1))
        for i in range(len(X)):
            if Y[i][0]*(X[i]*self.theta[:-1]+self.theta[-1])<=0:
                self.theta[:-1]=self.theta[:-1]+np.matrix(self.learn*Y[i][0]*X[i]).T
                self.theta[-1]=self.theta[-1]+self.learn*Y[i][0]
                i=0
                continue


Test = preceptron(0.001)
x = np.matrix([[1, 2], [2, 3], [4, 5]])
print(x.shape)
y = np.matrix([1, -1, -1]).reshape(-1,1)
print(y.shape)
Test.train_learn(x, y)
print(Test.theta)