import ScriptsOLD.Database as db
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

def normalize_column(col):
    m = col.shape[0]
    mu = np.mean(col, axis=0)
    sigma = np.std(col, axis=0)
    X = (col - mu) / sigma
    return np.reshape(X, (m, 1))

def plot_series(time, series, format="-", start=0, end=None, label=None):
    plt.plot(time[start:end], series[start:end], format, label=label)
    plt.xlabel("Time")
    plt.ylabel("Value")
    if label:
        plt.legend(fontsize=14)
    plt.grid(True)
    plt.show()


def plot_prediction(x, actual, prediction, title):
    plt.figure(figsize=(15, 8))
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title(title)
    plt.plot(x[0:150], actual[0:150], label="Actual")
    plt.plot(x[1:151], prediction[1:151], label="Prediction")
    plt.xticks(rotation="90")
    plt.legend()
    plt.show()

def clean_data():
    DATA = db.load_data()
    DATA.drop(DATA.index[:21850], inplace=True)
    X = np.ones((DATA.shape[0], 1))
    time = DATA.pop('Date')
    # for column in DATA.columns:
    #     X = np.concatenate([X, normalize_column(DATA[column].to_numpy())], axis=1)
    # return X.astype(np.float32), time.to_numpy()
    return DATA['Adj Close'].to_numpy(), time.to_numpy()

def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.SimpleRNN(100, return_sequences=True),
        tf.keras.layers.SimpleRNN(100)
    ])


def moving_average_forecast(series, window_size):
  """Forecasts the mean of the last few values.
     If window_size=1, then this is equivalent to naive forecast
     This implementation is *much* faster than the previous one"""
  mov = np.cumsum(series)
  mov[window_size:] = mov[window_size:] - mov[:-window_size]
  return mov[window_size - 1:-1] / window_size


def naive_forcast(X, time):
    split = len(X) - 250
    time_train = time[:split]
    x_train = X[:split]
    time_valid = time[split:]
    x_valid = X[split:]

    naive_pred = X[split - 1: -1]

    mae = tf.keras.metrics.mean_absolute_error(x_valid, naive_pred).numpy()
    print("Naive Forecasting Mean Absolute Error: {}".format(mae))
    # plot_prediction(time, x_valid, naive_pred, "Naive Forecasting")


def moving_average(X, time):
    split = len(X) - 250
    time_train = time[:split]
    x_train = X[:split]
    time_valid = time[split:]
    x_valid = X[split:]
    moving_avg = moving_average_forecast(X, 30)[split - 30:]

    mae = tf.keras.metrics.mean_absolute_error(x_valid, moving_avg).numpy()
    print("Naive Forecasting Mean Absolute Error: {}".format(mae))

    plt.figure(figsize=(10, 6))
    plot_series(time_valid, x_valid, label="Series")
    plot_series(time_valid, moving_avg, label="Moving average (30 days)")

def main():
    X, time = clean_data()
    # naive_forcast(X, time)
    moving_average(X, time)
    # X_train, X_test = X[:split], X[split:]
    # adj_close = X[:, 5]
    # plt.figure(figsize=(12, 6))
    # plt.plot(adj_close)
    # plt.show()