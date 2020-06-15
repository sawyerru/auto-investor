import requests
import datetime as dt
import yahooquery as yq
import fbchat
import twilio.rest as twilio
import os
import holidays
import pandas as pd
import json

TICKER = 'SABR'


def is_trading_day(today):
    return (dt.date(today.year, today.month, today.day).isoweekday() <= 5 and
    dt.date(today.year, today.month, today.day) not in holidays.UnitedStates())


def get_prev_trading_day_from(day=None, adjclose=False):
    ticker = yq.Ticker(TICKER)

    # go back in time to find previous trading day
    day = day - dt.timedelta(days=1)
    while not is_trading_day(day):
        day = day - dt.timedelta(days=1)

    data = ticker.history(start=day, end=day+dt.timedelta(days=1), period='1d') if day else ticker.history(period='5y')
    data = data['adjclose'].array[0] if adjclose else data
    return data, "SUCCESSFULLY RETRIEVED DATA FROM YAHOO\n"

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
    cookies = {}
    try:
        client = fbchat.Client(email=os.getenv("FB_USERNAME"),
                               password=os.getenv("FB_PASSWORD"),
                               session_cookies=cookies)
        datetime = get_current_timestep()
        text = datetime['full'] + '\t\n\n'
        text += body

        # Personal FB UID (Sawyer Ruben)
        UID = int(os.getenv("FB_UID"))
        with open('session.json', 'w') as f:
            json.dump(client.getSession(), f)
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

