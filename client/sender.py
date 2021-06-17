import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACebe1a15d4960a6ad8952f789e3f96f82'
auth_token = 'ff13483e6f0836dc94ff422776756fe3'
client = Client(account_sid, auth_token)

def send(bod='', to=''):
    message = client.messages \
                    .create(
                        body='\n{}'.format(bod),
                        from_='+17272058768',
                        to='+244{}'.format(to) 
                    )

    print(message.sid)
