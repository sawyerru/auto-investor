from pymongo import MongoClient


# DB_CONNECTION_STRING = "mongodb+srv://sruben:Ruben-5AW@cluster0-jr48x.mongodb.net/test?retryWrites=true&w=majority"
# DB = MongoClient(DB_CONNECTION_STRING).financials


def connect_to_db():
    # cnx = mysql.connector.connect(user='sawyerru', password='Ruben-5AW',
    #                               host='127.0.0.1',
    #                               database='fin')
    # return cnx
    print("Connected to MySQL")
