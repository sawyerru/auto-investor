import Scripts.Database as Database
import Scripts.Service as Service
import Scripts.Trading as Trading
import Algorithms.MultilayerPerceptron as MLP

import time
import datetime as dt
import holidays

def day_end():
    # Connect to DB
    # Pull Data from yahoo
    # Insert into table
    # pull table as X
    # Train Model
    # Create prediction
    Database.connect_to_db()
    prediction = MLP.run()
    Service.send_update("day end work")
    return prediction


def day_start(prediction):
    # read prediction
    print(prediction)
    # Initiate Trade logic
    Trading.connect_to_trading()
    # Trade
    Service.send_update("day start work")
    return


def main():

    print("Started at: ", dt.datetime.now())

    while True:
        today = dt.datetime.now()

        # Is Trading Day (is weekday and not holiday)
        if dt.date(today.year, today.month, today.day).isoweekday() <= 5 and \
                dt.date(today.year, today.month, today.day) not in holidays.UnitedStates():

            prediction = day_end()  # execute at 17:00
            # time.sleep(60*60*16)     # wait for 60seconds * 60minutes * 16hours
            day_start(prediction)   # execute at 9:00

        else:
            Service.send_update("Markets are closed today")



if __name__ == "__main__":
    main()
