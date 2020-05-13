# from yahoofinancials import YahooFinancials
# # import json
# # import requests
# def get_data(ticker):
#     # querystring = {"datatype": "json",
#     #                }
#     # response = requests.request("GET", BASE_URL, headers=HEADERS, params=querystring)
#     # print(response.text)
#     ticker = 'AAPL'
#     yahoo_financials = YahooFinancials(ticker)
#     print(yahoo_financials.get_stock_price_data())
#
# class Ticker:
#     """
#     Simple Class to hold company financial data
#     """
#     symbol = ''
#     obj = {}
#     def __init__(self, sym: str):
#         self.symbol = sym
#         # self.obj = YahooFinancials(sym)
#
#     # def __repr__(self):
#     #     # return self.obj.get_financial_stmts("annual", "cash")
