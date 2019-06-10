from twilio.rest import Client
import smtplib

# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234"
TWILIO_PHONE_NUMBER = '+13147204716'

# list of one or more phone numbers to dial, in "+19732644210" format
DIAL_NUMBERS = ["+12066379757"]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
account_sid = "AC05a87525715b6107358e7b7375d3d176"
auth_token = "cbe162e5017acdcf83ea532f0737d408"
client = Client(account_sid, auth_token)


def dial_numbers():
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in DIAL_NUMBERS:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")

def send_message():
    message = client.messages \
    .create(
         body = 'Your friend, David, is in danger! Send Help ASAP!',
         from_= TWILIO_PHONE_NUMBER,
         to= '+12066379757'
     )
    print('Message Sent')
    
def send_email():
  
    to = 'cvecheka07@gmail.com'
    gmail_user = 'impactalert59@gmail.com'
    gmail_pwd = 'Impact123!'
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo() # extra characters to permit edit
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
    #print(header)
    msg = header + '\n Testing from IMPACT\n\n'
    smtpserver.sendmail(gmail_user, to, msg)
    print('Email Sent!')
    smtpserver.quit()
 

#if __name__ == "__main__":
 #   dial_numbers(DIAL_NUMBERS)