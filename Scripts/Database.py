from pymongo import MongoClient
from pprint import pprint
import json
import numpy as np

DB_CONNECTION_STRING = "mongodb+srv://sruben:Ruben-5AW@cluster0-jr48x.mongodb.net/test?retryWrites=true&w=majority"
DB = MongoClient(DB_CONNECTION_STRING).financials

def connect_to_db():
    client = MongoClient(DB_CONNECTION_STRING)
    db = client.financials
    return db

def get_company(db, ticker):
    doc = db.companies.find_one({"Symbol": ticker})
    return doc

def get_historic_close_price(ticker):
    prices = []
    for record in DB.historic_price.find():
        prices.append(record['Adj Close'])
    return np.array(prices).T
