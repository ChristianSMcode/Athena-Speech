import utils.voice_synthesis as synth
from utils.record_audio import record_audio_file
from utils.words_manipulation import compare_words_simil
import time

execution_mode=[
    'conversation',
    'media',
    'command',
    'assistance',
    'fileSystem'
]

def main():
    record_audio_file('activacion.wav',5,1,44100)
    respuesta='dkjfn nual athhena'
    for word in respuesta.split(' '):
        if compare_words_simil(word,'Athena') > 60:
            synth.generate_response_audio('En que modo deseas ejecutar')
            time.sleep(2)
            #Reconocimiento voz
            mode='conversation'
            if mode == 'conversation':
                synth.generate_response_audio('Escuchando en modo conversation, en que te puedo ayudar.')
            elif mode == 'media':
                synth.generate_response_audio('Escuchando en modo media, en que te puedo ayudar.')
            elif mode == 'command':
                synth.generate_response_audio('Escuchando en modo comando, en que te puedo ayudar.')
            elif mode == 'assistance':
                synth.generate_response_audio('Escuchando en modo asistencia, en que te puedo ayudar.')
            elif mode == 'fileSystem':
                synth.generate_response_audio('Escuchando en modo fileSytem, en que te puedo ayudar.')
            else:
                synth.generate_response_audio('Modo no disponible')
            

if __name__ == '__main__':
    main()
