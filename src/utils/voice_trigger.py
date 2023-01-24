import speech_recognition as sr
import os

def listen_activate(trigger_word,language):
    r= sr.Recognizer()
    with sr.Microphone() as source:
        audio= r.listen(source)
    try:
        text = r.recognize_google(audio,language=language)
        if trigger_word in text.lower():
            return True
    except:
        return False

def recognize_option(opts,language):
    r= sr.Recognizer()
    with sr.Microphone() as source:
        audio= r.listen(source)
    try:
        text = r.recognize_google(audio,language=language)
        for word in opts:
            if word in text.lower():
                return word
    except:
        return False