# -*- Coding: UTF-8 -*-
from twilio.twiml.voice_response import VoiceResponse


def message(request):
    resp = VoiceResponse()
    resp.say("朝だ！起きろー！！!", language="ja-JP", voice="Polly.Mizuki")
    print(str(resp))
