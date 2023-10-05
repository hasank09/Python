from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.auth_token = '00d7adcf7fd92c1d5c8890ceb0d4cd8e'
        self.account_sid = 'AC0a5a426f2de0e392a5a34c65328a2c64'

    def send_sms(self, alert):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=alert,
            from_='+15178528384',
            to='+923222007425'
        )
        print(message.status)
