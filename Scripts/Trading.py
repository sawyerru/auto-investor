from robin_stocks import *
import os

def connect_to_trading(message):
    try:
        access_token = login(os.getenv("ROBINHOOD_USERNAME"),
                         os.getenv("ROBINHOOD_PASSWORD"))['access_token']
        if bool(access_token):
            message += "ROBINHOOD CONNECTION SUCCESSFUL"
    except:
        message += "ERROR CONNECTING TO ROBINHOOD"
