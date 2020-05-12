import numpy as np


def feature_normalize(X):
    """
    Normalize the feature data using dataset X
    :param X: original dataset
    :return: normalized dataset matrix
    """
    pass


def compute_cost(X, y, theta):
    """
    Cost Function, J = 1/(2m) * SUM (i->m) (hypoth(xi) - yi)^2
    Goal is to minimize cost function
    :param X: Data --  m x (d+1)
    :param y: labels -- m x 1
    :param theta: weights -- m x 1
    :return: the cost of the function
    """
    m = np.shape(y)[1]
    J = 0
    hypoth = theta.T @ X
    for i in range(m):
        J += (hypoth[i] - y[i])**2
    return J/(2*m)


def gradient_descent(X, y):
    """
    Run gradient descent on Linear Regression to minimize error
    :param X: data
    :param y: labels
    :return: theta
    """
    theta = np.zeros();
    pass

def normal_equation(X, y):
    """
    Closed form solution for the minimized Cost function of Linear Regression
    :param X: data
    :param y: labels
    :return: minimized weights for X and y
    """
    theta = np.linalg.inv(X.T @ X) @ X.T @ y
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
    I = np.eye(feature_dim)
    theta = np.linalg.inv(X.T @ X + lam * I) @ X.T @ y
    return theta

