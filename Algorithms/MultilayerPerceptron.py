import tensorflow as tf
import numpy as np
from Algorithms.Nucleus import *


def split(X, y, amt=1000):
    X_train = X[:amt]
    X_test = X[amt:]
    y_train = y[:amt]
    y_test = y[amt:]
    return X_train, X_test, y_train, y_test

def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(units=100, activation='relu', input_dim=3),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model


def run():
    X, y = transform(get_data())
    X_train, X_test, y_train, y_test = split(X, y)
    model = create_model()
    model.fit(X_train, y_train, epochs=1000, verbose=1)

    prediction = []
    for i in range(len(X_test)):
        x_input = X_test[i].reshape((1,3))
        yhat = model.predict(x_input, verbose=0)
        prediction.append(yhat)
        print("Predicted: {} \nActual:    {}".format(yhat, y_test[i]))

    # mse = tf.keras.losses.MSE(y_test, np.asarray(prediction))
    loss = np.mean(np.square(y_test-np.asarray(prediction)))
    print(loss)