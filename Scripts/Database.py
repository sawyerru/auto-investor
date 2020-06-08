from pymongo import MongoClient
import os


def connect_to_db(message):

    try:
        client = MongoClient("mongodb://{user}:{password}@{host}:{port}/test".format(
            user=os.getenv("MONGO_USER"),
            password=os.getenv("MONGO_PASSWORD"),
            host=os.getenv("MONGO_HOST"),
            port=os.getenv("MONGO_PORT")))
        db = client.test
        message += "MONGO CONNECTED SUCCESSFULLY\n"
        return db

    except:
        message += "Connection Error Occurred During Mongo Open\n"


