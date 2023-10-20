import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("boston.csv")
labels = np.asarray(data.columns)
print(labels)
print(type(labels))
print(type(data))
x = data.iloc[:100, :-1]
y = data.iloc[:100, -1]
x = np.asarray(x)
y = np.asarray(y)
# print(x)

for i in range(x.shape[1]):
    plt.scatter(x[:, i], y)
    plt.xlabel(labels[i])
    plt.ylabel(labels[-1])
    plt.show()


