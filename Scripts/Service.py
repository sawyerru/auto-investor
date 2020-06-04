import requests
import datetime as dt
import yahooquery as yq
import fbchat



def get_current_timestep():
    d = dt.datetime.now()
    full = "{}-{:0>2d}-{:0>2d} {:0>2d}:{:0>2d}:{:0>2d}".format(
        d.year, d.month, d.day, d.hour, d.minute, d.second)
    split = full.split()
    datetime = dict()
    datetime['full'] = full
    datetime['date'] = split[0]
    datetime['time'] = split[1]
    return datetime


def send_update(body):
    """
    Send message to self from FaceBook Bot
    :param body: text to be send
    :return: send notification to FB Messenger
    """
    # Logging into Bot
    client = fbchat.Client(email="3076319202", password="Ruben-5AW")
    datetime = get_current_timestep()
    text = datetime['full'] + '\t\n\n'
    text += body

    # Personal FB UID (Sawyer Ruben)
    UID = 100005957644239
    client.send(fbchat.Message(text=text), thread_id=UID, thread_type=fbchat.ThreadType.USER)
    client.logout()







