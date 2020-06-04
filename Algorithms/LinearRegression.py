import numpy as np


def compute_cost(X, y, theta):
    """
    Cost Function, J = 1/(2m) * SUM (i->m) (hypoth(xi) - yi)^2
    Goal is to minimize cost function
    :param X: Data --  m x (d+1)
    :param y: labels -- m x 1
    :param theta: weights -- m x 1
    :return: the cost of the function
    """
    m = y.size
    hypoth = np.dot(X, theta)
    J = (1/(2*m)) * np.sum(np.square(np.dot(X, theta) - y))
    return J


def gradient_descent(X, y, theta, alpha, num_iters):
    """
    Run gradient descent on Linear Regression to minimize error
    :param X: data
    :param y: labels
    :return: theta
    """
    m = y.shape[0]
    theta = theta.copy()
    J_History = []

    for i in range(num_iters):
        J_History.append(compute_cost(X, y, theta))
    return theta, J_History

def normal_equation(X, y):
    """
    Closed form solution for the minimized Cost function of Linear Regression
    :param X: data
    :param y: labels
    :return: minimized weights for X and y
    """
    theta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)
    return theta

def normal_equation_regularized(X, y, lam=1e-17):
    """
    Compute the model vector when we use l2-norm regularization
    theta = (X^T X + lambda I)^(-1) X^T t
    :param X: Nx(d+1) matrix
    :param y: Nx1 vector
    :param lam: the scalar regularization parameter, lambda
    :return: theta (d+1)x1 model vector
    """
    feature_dim = X.shape[1]
    L = np.eye(feature_dim)
    L[0][0] = 0
    theta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X) + lam * L), X.T), y)
    return theta

