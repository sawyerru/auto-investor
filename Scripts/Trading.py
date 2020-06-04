from robin_stocks import *

def connect_to_trading():
    print("Connected to Robinhood")


def login_to_account(username: str, password: str) -> bool:
    access_token = login(username, password)['access_token']
    return bool(access_token)