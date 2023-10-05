# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC0a5a426f2de0e392a5a34c65328a2c64"
auth_token = "00d7adcf7fd92c1d5c8890ceb0d4cd8e"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15005550006',
                     to='+923222007425'
                 )

print(message.sid)
