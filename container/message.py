# -*- Coding: UTF-8 -*-
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/message", methods=["GET", "POST"])
def message():
    resp = VoiceResponse()
    resp.say("朝だ！起きろー！！!", language="ja-JP", voice="Polly.Mizuki")
    return str(resp)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
