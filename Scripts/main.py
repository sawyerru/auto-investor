from robin_stocks import *


def login_to_account(username, password):
    access_token = login(username, password)['access_token']
    return bool(access_token)


def main():
    logged_in = login_to_account("sawyer.ruben@gmail.com", "Hotrod17!saw")
    if logged_in:
        stocks = build_holdings()
        for k, v in stocks.items():
            print(k, v)

        order_buy_market("GIS", 1)



if __name__ == "__main__":
    main()