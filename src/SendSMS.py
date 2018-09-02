
# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
import os

from data import TWILIO_ACCESS_ID, TWILIO_AUTH_TOKEN

twilio_access_id = TWILIO_ACCESS_ID
twilio_auth_token = TWILIO_AUTH_TOKEN


def send_sms(message):
    # the following line needs your Twilio Account SID and Auth Token
    client = Client(twilio_access_id, twilio_auth_token)
    #  change the "from_" number to your Twilio number and the "to" number
    #  to the phone number you signed up for Twilio with, or upgrade your
    #  account to send SMS to any phone number
    client.messages.create(to="+91 95662 45953", from_="+19169150142 ",body=message)
    return


if __name__ == "__main__":
    message = "Hi, Vijay"
    send_sms(message)