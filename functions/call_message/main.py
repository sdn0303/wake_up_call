# -*- Coding: UTF-8 -*-
from twilio.twiml.voice_response import VoiceResponse


def message(request):
    print(request.get_json())

    resp = VoiceResponse()
    resp.say("朝だ！起きろおおおおおお！", language="ja-JP", voice="Polly.Mizuki")
    print(str(resp))

    return str(resp)
