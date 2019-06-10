from twilio.rest import Client
TWILIO_PHONE_NUMBER = '+13147204716'

account_sid = "AC05a87525715b6107358e7b7375d3d176"

auth_token = "cbe162e5017acdcf83ea532f0737d408"

client = Client(account_sid, auth_token)
message = client.messages \
    .create(
         body='This is testing to see if twilio sends message to a specific phone number',
         from_= TWILIO_PHONE_NUMBER,
         to='+12066379757'
     )
print(message.sid)

