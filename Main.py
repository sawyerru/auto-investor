import Scripts.Database as Database
import Scripts.Service as Service
import Scripts.Trading as Trading
import Algorithms.MultilayerPerceptron as MLP

import time
import schedule
import datetime as dt
import holidays
import os

def day_end(prediction):
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


def day_start(prediction):
    message = "Trading Day beginning:\n\n"
    # read prediction
    message += "Predicted Price: ${}".format(prediction)
    # Initiate Trade logic
    Trading.connect_to_trading(message)
    # Trade
    Service.send_update(message)



def main():

    # Gather All Environment Variables into system
    file = open('env.txt', 'r')
    for line in file:
        obj = line.strip('\n').split('=')
        if len(obj) == 2:
            os.environ[obj[0]] = obj[1]


    print("Started at: ", dt.datetime.now())

    # Schedule operations and define shared variables
    prediction = None
    schedule.every().day().at("9:15").do(day_start, prediction)
    schedule.every().day().at("4:30").do(day_end, prediction)


    while True:
        today = dt.datetime.now()

        # Is Trading Day (is weekday and not holiday)
        if dt.date(today.year, today.month, today.day).isoweekday() <= 5 and \
                dt.date(today.year, today.month, today.day) not in holidays.UnitedStates():

            schedule.run_pending()
            time.sleep(1)

        else:
            Service.send_update("Markets are closed today")


if __name__ == "__main__":
    main()
