import speech_recognition as sr

def listen_activate():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something')
        audio= r.listen(source)
    try:
        text = r.recognize_google(audio,language="en-US")
        if "activate" in text.lower():
            print('Activated')
    except:
        print('I didnt understand')

#listen_activate()
#==========================================
execution_mode=[
    'conversation',
    'media',
    'command',
    'assistance',
    'fileSystem'
]

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

#print(recognize_option(execution_mode))