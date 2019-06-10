from twilio.twiml.voice_response import Dial, VoiceResponse, Say

response = VoiceResponse()
response.dial('206-637-9757')
response.say('Goodbye')

print(response)
