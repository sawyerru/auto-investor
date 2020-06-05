import requests
import datetime as dt
import yahooquery as yq
import fbchat
import twilio.rest as twilio
import os



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

    fb_username = os.getenv("FB_USRNAME")
    fb_password = os.getenv("FB_PASSWORD")
    # Logging into Bot
    try:
        client = fbchat.Client(email=fb_username, password=fb_password)
        datetime = get_current_timestep()
        text = datetime['full'] + '\t\n\n'
        text += body

        # Personal FB UID (Sawyer Ruben)
        UID = 100005957644239
        client.send(fbchat.Message(text=text), thread_id=UID, thread_type=fbchat.ThreadType.USER)
        client.logout()

    except:
        account_sid = 'AC2166d72c156e245ac17fdee2a57f1f72'
        auth_token = '843869672ac223bbf0161df2706f98e3'
        client = twilio.Client(account_sid, auth_token)

        message = client.messages.create(
            body="ERROR logging into Albert Facebook",
            from_='+12092314126',
            to='+13076319202'
        )

