import time as tm

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class linearRegression:
    """python语言实现线性回归算法。（梯度下降实现）"""

    def __init__(self, alpha, times, eps):
        """初始化方法

        Parameters：
        ----------------------
        alpha：float
               学习率，用来控制步长。（权重调整的幅度）
        times： int
                循环迭代的次数。

        """
        self.alpha = alpha
        self.times = times
        self.eps = eps
        # 创建权重向量，初始值为0（或任何其他值），长度比特征数量多1（多出的就是截距）。

    def fit(self, X, y):
        """根据提供的训练数据，对模型进行训练

        Parameters:
        -----------------
        X：类数组类型。形状：[样本数量，特征数量]
           特征矩阵，用来对模型进行训练。
        y：类数组类型，形状：[样本数量]
          目标值（标签信息）。
          self.w_:参数矩阵
        theta_history：记录迭代过程
        loss_history：记录迭代的损失值
        X:n维，  n=X.shape[1],m*n,纯数据
        theta:n+1维,(n+1)*1
        Mat_X :n+1维,m*(n+1),加了一个常数项1的一列
        y:1维，m*1,
        mat_y:1维，m*1
        """

        # self.w_ = np.zeros(1 + X.shape[1]) # 9*1
        self.w_ = np.random.rand(X.shape[1] + 1)
        # 创建损失列表，用来保存每次迭代后的损失值，损失值计算：（预测值 - 真实值）的平方和除以2.
        self.loss_ = []
        X = np.asarray(X)  # 800*8
        y = np.asarray(y)  # 800*1
        self.w_ = np.asarray(self.w_)
        w_history = np.zeros((self.times, X.shape[1] + 1))

        # 进行循环多次迭代，在每次迭代过程中，不断调整权重值，使得损失值不断下降。
        i = 0
        eps = 10
        while i < self.times:
            # 计算预测值 y = w0 + w1*x1 + w2*x2 ...
            # 800*8 8*1 +1*1
            y_hat = np.dot(X, self.w_[1:]) + self.w_[0]
            # 计算真实值与预测值之间的差距。
            error = y - y_hat
            # 计算损失值 损失值计算：（预测值 - 真实值）的平方和除以2
            self.loss_.append(np.sum(error ** 2) / 2)
            g = np.dot(X.T, error)
            eps = np.linalg.norm(g)
            if eps > self.eps:
                # 根据差距调整权重w_，根据公式：调整为 权重(j) = 权重(j) + 学习率*sum((y-y_hat)*x(j))
                self.w_[0] += self.alpha * np.sum(error * 1) / X.shape[0]
                self.w_[1:] += self.alpha * np.dot(X.T, error) / X.shape[0]
                w_history[i, :] = self.w_
            else:
                break

        return w_history

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

        X = np.asarray(X)
        result = np.dot(X, self.w_[1:]) + self.w_[0]
        return result


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
# 打乱原始数据
t = data.sample(len(data), random_state=0)
# 产生训练集与测试集
train_X5 = t.iloc[:350, 5]
train_X12 = t.iloc[:350, 12]
train_y = t.iloc[:350, -1]
test_X5 = t.iloc[350:, 5]
test_X12 = t.iloc[350:, 12]
test_y = t.iloc[350:, -1]
# print(train_X5)
# print(train_X12)
train_X = np.stack((train_X5, train_X12)).T
# print(train_X)
test_X = np.stack((test_X5, test_X12)).T

lr = linearRegression(alpha=0.05, times=10000, eps=10 ** (-5))
# 标准化处理
s = StandardScaler()
train_X = s.fit_transform(train_X)
test_X = s.fit_transform(test_X)

s2 = StandardScaler()
train_y = s2.fit_transform(train_y)
test_y = s2.fit_transform(test_y)

# 训练 预测
time_start = tm.time()
history = lr.fit(train_X, train_y)
time_end = tm.time()
print(time_end - time_start)
# print(history)
result = lr.predict(test_X)
x = result - np.asarray(test_y)
print(np.mean(np.square(x)) / 2)
print(lr.w_)
# print(lr.loss_)

plt.figure(figsize=(10, 10))
plt.plot(result, "ro-", label="predict")
plt.plot(test_y.values, "go-", label="true")  # pandas读取时serise类型，我们需要转为ndarray
plt.title("Gradient_descent")
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
