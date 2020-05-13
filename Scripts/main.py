from robin_stocks import *

import Algorithms.LinearRegression as linear
from Scripts.Ticker import *
import Scripts.Database as db


def login_to_account(username: str, password: str) -> bool:
    access_token = login(username, password)['access_token']
    return bool(access_token)


def main():
    # logged_in = login_to_account("sawyer.ruben@gmail.com", "Hotrod17!saw")
    # if logged_in:
    #     stocks = build_holdings()
    #     for k, v in stocks.items():
    #         print(k, v)
    database = db.connect_to_db()
    doc = db.get_company(database, 'SPY')
    db.get_historic_close_price('SPY')
    print(doc)







if __name__ == "__main__":
    main()