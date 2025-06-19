from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    response = VoiceResponse()
    response.say("Hello, this is Steve Perry's AI assistant speaking. Leave a message or press any key.", voice='Polly.Joanna')
    return Response(str(response), mimetype='text/xml')

@app.route("/")
def home():
    return "Twilio Answer Call Server Running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)