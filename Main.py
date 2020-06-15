import Scripts.Database as Database
import Scripts.Service as Service
import Scripts.Trading as Trading
import Algorithms.MultilayerPerceptron as MLP
import Algorithms.ConvolutionalNeuralNet as CNN
import Algorithms.LongShortTermMemory as LSTM
import Algorithms.EncoderDecoder as ENCDEC
import Algorithms.CNN_LSTM as CNN_LSTM

import time
import schedule
import datetime as dt
import random

import os
import sys


def day_start(prediction):
    today = dt.datetime.today()

    if Service.is_trading_day(today):

        message = "Trading Day beginning:\n\n"
        # read prediction and previous price
        prev_close, m = Service.get_prev_trading_day_from(today)
        message += "Predicted Close: ${:.2f} \n Previous Close: ${:.2f}\n".format(prediction, prev_close)

        # Initiate Trade logic
        m = Trading.connect_to_trading()
        message += m

        # Price decrease, we sell in the morning before the slide
        if prediction < prev_close:
            # m = Trading.sell()
            message += m
        # Price increase, we buy in the morning before the climb
        if prediction > prev_close:
            # m = Trading.buy()
            message += m

        Service.send_update(message)
        Trading.logout()
    else:
        Service.send_update("\nMarkets are closed today")


def day_end(prediction):
    today = dt.datetime.today()

    # Is Trading Day (is weekday and not holiday)
    if Service.is_trading_day(today):

        message = "Trading Day completed:\n\n"
        # Display day close and day prediction:
        prev_close = Service.get_prev_trading_day_from(day=today, adjclose=True)
        message += "Predicted Close: ${:.2f} \n Closed At: ${:.2f}".format(prediction, prev_close)

        # Connect to Database Server
        col, m = Database.connect_to_db()
        message += m

        # Pull Data from yahoo and write to Database
        m = Database.write(Service.get_prev_trading_day_from(day=today, adjclose=False))
        message += m

        # Retrieve Features in arranged data and Train Model
        features = Database.retrieve_data(col)
        prediction, m = MLP.run(features, prediction)
        message += m
        Service.send_update(message)
    else:
        Service.send_update("\nMarkets are closed today")


def main():

    # Gather All Environment Variables into system
    file = open(sys.argv[1], 'r')
    for line in file:
        obj = line.strip('\n').split('=')
        if len(obj) == 2:
            os.environ[obj[0]] = obj[1]

    print("Started at: ", dt.datetime.now())
    print(os.environ)

    # Schedule operations and define shared variables
    prediction = 0
    # schedule.every().day.at("09:15").do(day_start, prediction)
    # schedule.every().day.at("16:30").do(day_end, prediction)

    while True:
        # schedule.run_pending()
        day_start(prediction)
        day_end(prediction)
        # time.sleep(1)


if __name__ == "__main__":
    main()
