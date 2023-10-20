import random as rd
import time as tm

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class LinearRegression:
    '''
    牛顿法实现多元线性回归
    '''

    def __init__(self, eps, times):
        """
        参数定义:
        eps：精度
        times；迭代次数
        """
        self.theta = None
        self.eps = eps
        self.times = times

    def fit_newton(self, X, y):
        """根据提供的训练数据，对模型进行训练

        Parameters:
        -----------------
        X：类数组类型。形状：[样本数量，特征数量]
           特征矩阵，用来对模型进行训练。
        y：类数组类型，形状：[样本数量]
          目标值（标签信息）。

        theta:参数矩阵
        theta_history：记录迭代过程
        loss_history：记录迭代的损失值
        X:n维，  n=X.shape[1],m*n
        theta:n+1维,(n+1)*1
        Mat_X :n+1维,m*(n+1)
        y:1维，m*1,
        mat_y:1维，m*1
        """
        self.theta = np.random.rand(X.shape[1] + 1).reshape(-1, 1)
        for i in range(self.theta.shape[0]):
            self.theta[i, 0] = rd.random()
        Mat_ones = np.ones((len(X), 1))
        Mat_X = np.hstack((Mat_ones, X))
        Mat_y = np.asarray(y).reshape(-1, 1)
        theta_history = np.zeros((self.times, (X.shape[1] + 1)))
        loss_history = np.zeros(self.times)
        self.loss_ = []
        i = 0
        while i < self.times:
            """
            i 记录次数
            eps 精度记录
            """
            # 计算真实值与预测值之间的差距。
            y_hat = np.dot(Mat_X, self.theta)
            error = y_hat - Mat_y
            # 计算损失值 损失值计算：（预测值 - 真实值）的平方和除以2
            self.loss_.append(np.sum(error ** 2) / 2)
            # 一阶导数
            g = (np.dot(np.dot(Mat_X.T, Mat_X), self.theta) - np.dot(Mat_X.T, Mat_y))
            # 黑塞矩阵
            h = np.dot(Mat_X.T, Mat_X)
            # 计算精度
            eps = np.linalg.norm(g)
            if eps > self.eps:
                # 计算theta
                self.theta = self.theta - np.dot(np.linalg.inv(h), g)
                theta_history[i, :] = self.theta.T

            else:
                break
            i += 1
        return theta_history

    def predict(self, X):
        """根据参数传递的样本，对样本数据进行预测

        Parameters:
        -----------------
        X：类数组类型。形状：[样本数量，特征数量]
           待测试样本。

        Return:
        -----------------
        result：数组类型
               预测的结果。
        """

        Mat_ones = np.ones((len(X), 1))
        Mat_X = np.hstack((Mat_ones, X))
        result = np.dot(Mat_X, self.theta)
        return result


def rmse(predict, test):
    test = np.asarray(test).reshape(-1, 1)
    MSE = np.sum(np.power((predict - test.reshape(-1, 1)), 2)) / len(test)
    rmse = np.sqrt(MSE)
    return rmse


class StandardScaler:
    """该类对数据进行标准化处理。每一列变为标准正态分布 X~N(0,1.ipynb_checkpoints)"""

    def fit(self, X):
        """根据传递的样本，计算每个特征列的均值与标准差

       Parameters：
        X: 类数组类型
           训练数据，用来计算均值与标准差
        """

        X = np.asarray(X)
        # axis=0 按列
        self.std_ = np.std(X, axis=0)
        self.mean_ = np.mean(X, axis=0)

    def transform(self, X):
        """对给定的数据X进行标准化处理，将X的每一列都变成标准正态分布的数据。

        Parameters：
        X: 类数组类型
           待转换数据。

        Return:
        result: 类数组类型
               参数X转换成标准正态分布后的结果。
        """

        return (X - self.mean_) / self.std_

    def fit_transform(self, X):
        """对数据进行训练，并转换，返回转换之后的结果

        Parameters：
        X: 类数组类型
           待转换数据。

        Return:
        result: 类数组类型
               参数X转换成标准正态分布后的结果。

        """
        self.fit(X)
        return self.transform(X)


data = pd.read_csv("boston.csv")
t = data.sample(len(data), random_state=0)
train_X5 = t.iloc[:400, 5]
train_X12 = t.iloc[:400, 12]
train_y = t.iloc[:400, -1]
test_X5 = t.iloc[400:, 5]
test_X12 = t.iloc[400:, 12]
test_y = t.iloc[400:, -1]
# print(train_X5)
# print(train_X12)
train_X = np.stack((train_X5, train_X12)).T
# print(train_X)
test_X = np.stack((test_X5, test_X12)).T

lr = LinearRegression(eps=10 ** (-10), times=10000)
# 标准化处理
s = StandardScaler()
train_X = s.fit_transform(train_X)
test_X = s.fit_transform(test_X)

s2 = StandardScaler()
train_y = s2.fit_transform(train_y)
test_y = s2.fit_transform(test_y)

# 训练 预测
time_start = tm.time()
theta_history = lr.fit_newton(train_X, train_y)
time_end = tm.time()
print(time_end - time_start)
result = lr.predict(test_X)
# RMSE = rmse(result, test_y)
x = np.asarray(test_y) - result
print(np.mean(np.square(x)) / 2)
print(np.hstack(lr.theta))
# print(theta_history)
print(lr.loss_)

plt.figure(figsize=(10, 10))
plt.plot(result, "ro-", label="predict")
plt.plot(test_y.values, "go-", label="True")  # pandas读取时serise类型，我们需要转为ndarray
plt.title("Function-ND")
plt.xlabel("xi")
plt.ylabel("house value")
plt.legend()
plt.show()

# 绘制累计误差
plt.plot(range(1, len(lr.loss_) + 1), lr.loss_, "o-", label="loss_sum")
plt.xlabel("times")
plt.ylabel("loss_sum")
plt.legend()
plt.show()
