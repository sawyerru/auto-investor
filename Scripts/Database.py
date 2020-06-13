from pymongo import MongoClient
import pandas as pd
import os


def connect_to_db():

    try:
        client = MongoClient("mongodb://{user}:{password}@{host}:{port}/financials".format(
            user=os.getenv("MONGO_USER"),
            password=os.getenv("MONGO_PASSWORD"),
            host=os.getenv("MONGO_HOST"),
            port=os.getenv("MONGO_PORT")))
        db = client.financials
        return db, "MONGO CONNECTED SUCCESSFULLY\n"

    except:
        return "Connection Error Occurred During Mongo Open\n"

def retrieve_data(db):
    data = pd.DataFrame(list(db.SABR.find({})))
    return data

def write(data):
    # db.SABR.insertDoc
    pass
