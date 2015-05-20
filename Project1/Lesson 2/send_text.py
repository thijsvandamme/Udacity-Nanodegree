from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC8839b68c4265616f0e80206c815c51e3"
auth_token  = "b2fced9f5d0100babbfe58a5f20be668"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="I love you baby!!",
    to="+12023046552",    # Replace with your phone number
    from_="+14437648430") # Replace with your Twilio number
print message.sid