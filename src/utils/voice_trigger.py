import speech_recognition as sr

def listen_activate(trigger_word):
    r= sr.Recognizer()
    with sr.Microphone() as source:
        audio= r.listen(source)
    try:
        text = r.recognize_google(audio,language="en-US")
        if trigger_word in text.lower():
            return True
    except:
        return False

def recognize_option(opts):
    r= sr.Recognizer()
    with sr.Microphone() as source:
        audio= r.listen(source)
    try:
        text = r.recognize_google(audio,language="en-US")
        for word in opts:
            if word in text.lower():
                return word
    except:
        return False