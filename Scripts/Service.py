import requests
import datetime as dt
import yahooquery as yq
import fbchat
import twilio.rest as twilio
import os


def pull_day(message):
    ticker = yq.Ticker('SABR')
    data = ticker.history(period='5y', interval='1d')
    message += "SUCCESSFULLY RETRIEVED DATA FROM YAHOO\n"
    return data

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
    try:
        client = fbchat.Client(email=os.getenv("FB_USERNAME"),
                               password=os.getenv("FB_PASSWORD"))
        datetime = get_current_timestep()
        text = datetime['full'] + '\t\n\n'
        text += body

        # Personal FB UID (Sawyer Ruben)
        UID = int(os.getenv("FB_UID"))
        client.send(fbchat.Message(text=text), thread_id=UID, thread_type=fbchat.ThreadType.USER)
        client.logout()

    except:
        account_sid = os.getenv('TWILIO_ACC_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        client = twilio.Client(account_sid, auth_token)

        message = client.messages.create(
            body="ERROR logging into Albert Facebook",
            from_='+12092314126',
            to=os.getenv('PHONE')
        )

