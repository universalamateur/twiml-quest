from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Create a route to handle incoming SMS messages
# It replies with a Sms message with the string returned
@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    print(f'Incoming message from {request.values.get("From")}: ${request.values.get("Body")}')

    # Generating TwiML using the Python helper library
    resp = MessagingResponse()
    resp.message("TwilioQuest rules")

    return str(resp)

# Receiving the status updates on the sent SMS
@app.route("/status", methods=["GET", "POST"])
def my_status_function():
    print(f"Message SID {request.values.get('MessageSid')} has a status of {request.values.get('MessageStatus')}")