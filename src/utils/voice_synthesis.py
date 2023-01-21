import pyttsx3

engine = pyttsx3.init()

# Personalizar configuraciones
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
engine.setProperty('language', 'es-ES')

# cambiar tipo de voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def generate_response_audio(*texts):
    if len(texts) <= 0:
        engine.say('Argument list must not be empty')
        engine.runAndWait()
    for text in texts:
        if not isinstance(text,str):
            engine.say('Argument must valid and string type')
            engine.runAndWait()
        engine.say(text)
        engine.runAndWait()


