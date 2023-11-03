import numpy as np


class perceptron:
    def __init__(self, learn, theta=None, bias=0):
        self.learn = learn
        self.theta = theta
        self.bias = bias
        self.alpha = 0
        self.loss = []

    def dual_learn(self, x, y):
        self.alpha = np.zeros(x.shape[0])
        is_wrong = False
        G = np.dot(x, x.T)
        while not is_wrong:
            wrong_count = 0
            loss = 0
            i = 0
            while i < len(x):
                y_i = y[i]
                a = []
                for j in range(len(x)):
                    a.append(self.alpha[j] * y[j])
                a = np.array(a)
                temp = np.dot(a, G[:, i])
                temp_sum = np.sum(temp)
                t = y_i * (temp_sum + self.bias)
                if t <= 0:
                    self.alpha[i] = self.alpha[i] + self.learn
                    self.bias = self.bias + self.learn * y_i
                    wrong_count += 1
                    loss += t
                else:
                    i += 1
            self.loss.append(-loss)
            if wrong_count == 0:
                is_wrong = True

    def origin_learn(self, x, y):
        self.theta = np.zeros(x.shape[1])
        self.bias = 0
        is_wrong = False
        while not is_wrong:
            wrong_count = 0
            i = 0
            loss = 0
            while i < len(x):
                y_i = y[i]
                temp = np.dot(self.theta, x[i])
                temp_sum = np.sum(temp)
                if y_i * (temp_sum + self.bias) <= 0:
                    self.theta = self.theta + self.learn * y_i * x[i]
                    self.bias = self.bias + self.learn * y_i
                    wrong_count += 1
                    loss += y_i * (temp_sum + self.bias)
                else:
                    i += 1
            self.loss.append(loss)
            if wrong_count == 0:
                is_wrong = True


x = np.array([[3, 3], [4, 3], [1, 1]])
y = np.array([1, 1, -1])
train = perceptron(1)
train.dual_learn(x, y)
print(train.loss)
print(train.alpha)
print(train.bias)
train = perceptron(1)
train.origin_learn(x, y)
print(train.loss)
print(train.theta)
print(train.bias)
