import utils.voice_synthesis as synth
from utils.voice_trigger import listen_activate,recognize_option
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
    while True:
        print('Activalo')
        if listen_activate('activate'):
            synth.generate_response_audio('En que modo deseas ejecutar')
            mode=recognize_option(execution_mode)
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
