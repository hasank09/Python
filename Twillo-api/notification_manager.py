from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.auth_token = 'Your_Twillo_AUT_Token'
        self.account_sid = 'Your_Account_sid'

    def send_sms(self, alert):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=alert,
            from_='+15178528384',
            to='+xxxdestinationnumber'
        )
        print(message.status)
