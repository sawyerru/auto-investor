from robin_stocks import *
import os


def connect_to_trading():
    try:
        access_token = login(os.getenv("ROBINHOOD_USERNAME"),
                         os.getenv("ROBINHOOD_PASSWORD"))['access_token']
        if bool(access_token):
            return "ROBINHOOD CONNECTION SUCCESSFUL"
    except:
        return "ERROR CONNECTING TO ROBINHOOD"


def buy():
    order_buy_market('SABR', 1)
    return "SUCCESSFUL PURCHASE"


def sell():
    order_sell_market('SABR', 1)
    return "SUCCESSFUL SALE"


def logout():
    logout()

