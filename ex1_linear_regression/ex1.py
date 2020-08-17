import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = "/home/jinyang/Code/ML_Andrew-Ng/ex1_linear_regression/ex1data1.txt"
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
data.head()  # 返回数据的前 n行，默认为5
data.insert(0, "Ones", 1)  # 为矩阵 X 添加一列 1
theta = np.matrix([0, 0])  # 初始化拟合参数

iterations = 1500

# 此时 X 为 m * 2 矩阵， theta.T 为 2 * 1 矩阵
alpha = 0.01

cols = data.shape[1]
X = data.iloc[:, :-1]  # 所有行，第一列到倒数第一列
X.head()  # 通过 h 函数计算 预测值

y = data.iloc[:, cols-1:cols]  # 所有行，最后一列
y.head()  # 实际值

theta = np.matrix([0, 0])


def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * X.shape[0])


X = np.matrix(X.values)
y = np.matrix(y.values)

computeCost(X, y, theta)


def gradientDescent(X, y, theta, alpha, iters):
    tmp = np.matrix(np.zeros(theta.shape))
    params = int(theta.ravel().shape[1])  # theta向量参数个数
    cost = np.zeros(iters)  # 记录每次迭代的代价

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(params):
            term = np.multiply(error, X[:, j])
            tmp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))

        theta = tmp
        cost[i] = computeCost(X, y, theta)

    return theta, cost


alpha = 0.01
iters = 1500

g, cost = gradientDescent(X, y, theta, alpha, iters)