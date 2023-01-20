import pyttsx3

def generate_response_audio(*texts):
    engine = pyttsx3.init()
    if len(texts) <= 0:
        engine.say('Argument list must not be empty')
        engine.runAndWait()
    for text in texts:
        if not isinstance(text,str):
            engine.say('Argument must valid and string type')
            engine.runAndWait()
        engine.say(text)
        engine.runAndWait()


