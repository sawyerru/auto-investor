# from matplotlib import pyplot
import numpy as np
import os
import pandas as pd
import yahooquery as yq

def get_data():
    t = yq.Ticker('SABR')
    data = t.history(period='5y')
    return data['adjclose'].to_numpy()

def transform(data):
    # data = get_data()
    window_size = 3
    X = []
    Y = []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size])
        Y.append([data[i+window_size]])
    X = np.array(X)
    Y = np.array(Y)
    assert len(X) == len(Y)
    return X, Y


def transform_4(data):
    data = get_data()
    window_size = 4
    X = []
    Y = []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size])
        Y.append([data[i+window_size]])
    X = np.array(X)
    Y = np.array(Y)
    assert len(X) == len(Y)
    return X, Y


def randomize(data):
    return np.random.shuffle(data)


def plot_data(X, y, theta):
    pyplot.figure()
    pyplot.plot(X[:, 1], y, 'ro', ms=10, mec='k')
    pyplot.plot(X[:, 1], np.dot(X, theta), '-')
    pyplot.legend(['Training data', 'Linear regression'])
    pyplot.show()


def load_data(filename):
    data = np.loadtxt(os.path.join('Data', filename), delimiter=',')
    m = data.shape[0]
    d = data.shape[1]
    X = data[:, 0:d-1]
    y = data[:, d-1]
    return X, y, m


def test_linear_reg(X, y):
    return AlgorithmsOLD.LinearRegression.normal_equation_regularized(X, y)


def test_logistic_reg(X, y):
    # return AlgorithmsOLD.LogisticRegression_
    pass


def main():
    X, y, m = load_data('ex1data1.txt')
    X_norm, mu, sigma = feature_normalize(X)
    theta = test_linear_reg(X_norm, y)
    plot_data(X_norm, y, theta)

