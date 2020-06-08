import Scripts.Database as Database
import Scripts.Service as Service
import Scripts.Trading as Trading
import Algorithms.MultilayerPerceptron as MLP

import time
import schedule
import datetime as dt
import random
import holidays
import os

def day_end(prediction):
    today = dt.datetime.now()

    # Is Trading Day (is weekday and not holiday)
    if dt.date(today.year, today.month, today.day).isoweekday() <= 5 and \
            dt.date(today.year, today.month, today.day) not in holidays.UnitedStates():

        message = "Trading Day completed:\n\n"
        # Connect to DB
        db = Database.connect_to_db(message)
        # Pull Data from yahoo
        data = Service.pull_day(message)
        # Insert into table
        # pull table as X
        # Train Model
        # Create prediction
        prediction = MLP.run(prediction, message)
        Service.send_update(message)
    else:
        Service.send_update("Markets are closed today")


def day_start(prediction):
    today = dt.datetime.now()

    # Is Trading Day (is weekday and not holiday)
    if dt.date(today.year, today.month, today.day).isoweekday() <= 5 and \
            dt.date(today.year, today.month, today.day) not in holidays.UnitedStates():

        message = "Trading Day beginning:\n\n"
        # read prediction
        message += "Predicted Price: ${}".format(prediction)
        # Initiate Trade logic
        Trading.connect_to_trading(message)
        # Trade
        Service.send_update(message)
    else:
        Service.send_update("Markets are closed today")



def main():

    # Gather All Environment Variables into system
    file = open('env.txt', 'r')
    for line in file:
        obj = line.strip('\n').split('=')
        if len(obj) == 2:
            os.environ[obj[0]] = obj[1]
        if len(obj) == 1:
            print("Error with environment variable file, be sure to fill out all fields")
            raise ValueError

    print("Started at: ", dt.datetime.now())

    # Schedule operations and define shared variables
    prediction = None
    schedule.every().day.at("09:15").do(day_start, prediction)
    schedule.every().day.at("16:30").do(day_end, prediction)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
