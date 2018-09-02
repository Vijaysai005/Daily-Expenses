
# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
import os

twilio_access_id = os.environ.get("TWILIO_ACCESS_ID", "AC9f8b37202cf9778852aa54b6f0a590d6")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN", "7bdc904f7d45c72e213f0e3736f4877b")


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