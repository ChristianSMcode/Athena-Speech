import utils.voice_synthesis as synth
from utils.voice_trigger import listen_activate,recognize_option
from utils.words_manipulation import compare_words_simil
import time

execution_mode=[
    'conversación',
    'media',
    'command',
    'assistance',
    'fileSystem'
]

def main():
    while True:
        print('Activalo')
        if listen_activate('actívate'):
            synth.generate_response_audio('En que modo deseas ejecutar')
            mode=recognize_option(execution_mode)
            if mode == 'conversación':
                synth.generate_response_audio('Escuchando en modo conversation.')
            elif mode == 'media':
                synth.generate_response_audio('Modo no disponible')
            elif mode == 'command':
                synth.generate_response_audio('Modo no disponible')
            elif mode == 'assistance':
                synth.generate_response_audio('Modo no disponible')
            elif mode == 'fileSystem':
                synth.generate_response_audio('Modo no disponible')
            else:
                synth.generate_response_audio('No entendí, intenta denuveo')

            

if __name__ == '__main__':
    main()
