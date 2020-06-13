import tensorflow as tf
import time
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


def run(X, prediction):
    # Data Arrangement
    X, y = transform(get_data())
    X_train, X_test, y_train, y_test = split(X, y)
    model = create_model()

    # Train Model
    start = time.perf_counter()
    model.fit(X_train, y_train, epochs=1000, verbose=1)
    end = time.perf_counter()

    # Create Prediction
    x_input = X_test[len(X_test)-1].reshape((1, 3))
    prediction = model.predict(x_input, verbose=0)

    # Format Logging
    log = """MLP Model trained in {:.5f} seconds\n
             MLP Model Loss: {}\n
             MLP Prediction: ${}\n""".format(start-end, model.loss, prediction)
    return prediction, log
