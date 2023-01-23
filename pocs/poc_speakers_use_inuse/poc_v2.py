import pyttsx3

engine = pyttsx3.init()

# Personalizar configuraciones
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
engine.setProperty('language', 'es-ES')

# cambiar tipo de voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Reproducir texto utilizando síntesis de voz
engine.say("hola soy nava, todo es una bendición")
engine.runAndWait()