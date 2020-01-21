# -*- Coding: UTF-8 -*-
import os

from twilio.rest import Client


def call_me():
    client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))
    return client.calls.create(
        to=os.getenv("MY_NUMBER"),
        from_=os.getenv("TWILIO_NUMBER"),
        url=os.getenv("URL_OF_MESSAGE")
    )


def alarm_call_pubsub(event, context):
    print(f"Event:          {event}")
    print(f"EventID:        {context.event_id}")
    print(f"EventTimeStamp: {context.timestamp}")

    call = call_me()
    return str(call.sid)
