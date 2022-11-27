# first install twillio using pip install twilio
# ctrl + shi + p to open command palette
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1bf9523755ca1bdad62bd43c9f2f8d9b"
# Your Auth Token from twilio.com/console
auth_token = "8929369d7f89bd416565da35f5d6b8fb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+251934947532",
    from_="+17816705483",
    body="Hello from Python!"
)
print(message.sid)
