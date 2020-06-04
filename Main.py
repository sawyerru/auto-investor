import Scripts.Database as Database
import Scripts.Service as Service
import Scripts.Trading as Trading
import Algorithms.MultilayerPerceptron as MLP

import datetime as dt
import holidays

def day_end():
    today = dt.datetime.now()

    # Is Trading Day (is weekday and not holiday)
    if dt.date(today.year, today.month, today.day).isoweekday() <= 5 and \
            dt.date(today.year, today.month, today.day) not in holidays.UnitedStates():
        print("day end work")
        Database.connect_to_db()
        Trading.connect_to_trading()
        MLP.run()
        Service.send_update("day end work")
    else:
        print("Markets are closed today")
    # Service.send_update("day end work")


def day_start():
    today = dt.datetime.now()

    # Is Trading Day (is weekday and not holiday)
    if dt.date(today.year, today.month, today.day).isoweekday() <= 5 and \
            dt.date(today.year, today.month, today.day) not in holidays.UnitedStates():
        print("day start work")
        Service.send_update("day start work")

    else:
        print("Markets are closed today")
        # Service.send_update("day start work")

def main():

    print("Started at: ", dt.datetime.now())
    day_start()
    day_end()

    # while True:
    #     day_start()
    #     day_end()
    #     time.sleep(60*5)
    #     print("Completing new cycle")


if __name__ == "__main__":
    main()
