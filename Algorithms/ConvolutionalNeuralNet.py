import tensorflow as tf
import numpy as np
from AlgorithmsOLD.Nucleus import *


def split(X, y, amt=300):
    X_train = X[:amt]
    X_test = X[amt:]
    y_train = y[:amt]
    y_test = y[amt:]
    return X_train, X_test, y_train, y_test

def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv1D(filters=64, kernel_size=2, activation='relu', input_shape=(3,1)),
        tf.keras.layers.MaxPooling1D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(units=50, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def main():
    X, y = transform(np.random.shuffle(get_data()))
    X_train, X_test, y_train, y_test = split(X, y)
    model = create_model()
    # reshape to [samples, subsequences, timesteps, features]
    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    model.fit(X_train, y_train, epochs=1000, verbose=1)

    prediction = []
    for i in range(len(X_test)):
        x_input = X_test[i].reshape((1, 3, 1))
        yhat = model.predict(x_input, verbose=0)
        prediction.append(yhat)
        print("Predicted: {} \nActual:    {}".format(yhat, y_test[i]))

    # mse = tf.keras.losses.MSE(y_test, np.asarray(prediction))
    loss = np.mean(np.square(y_test-np.asarray(prediction)))
    print(loss)
