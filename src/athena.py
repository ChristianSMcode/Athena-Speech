import utils.voice_synthesis as synth
from utils.voice_trigger import listen_activate,recognize_option
from utils.words_manipulation import compare_words_simil
import time
import random
import json
from dotenv import load_dotenv
import os

load_dotenv()

LANGUAGE=os.environ['LANGUAGE']
with open(f'metadata/languages/dictionary_{LANGUAGE}.json', encoding='utf-8') as file:
    configuration_json=json.load(file)

def main():
    while True:
        random_number=random.randint(0,2)
        print('Activalo')
        if listen_activate(configuration_json['activation_word'],LANGUAGE):
            
            synth.generate_response_audio(configuration_json['prompts']['initialization'][random_number])
            mode=recognize_option(configuration_json['execution_mode'],LANGUAGE)

            if mode == configuration_json['execution_mode'][0]:
                synth.generate_response_audio('Escuchando en modo conversation.')

            elif mode == configuration_json['execution_mode'][1]:
                synth.generate_response_audio('Modo no disponible')

            elif mode == configuration_json['execution_mode'][2]:
                synth.generate_response_audio('Modo no disponible')

            elif mode == configuration_json['execution_mode'][3]:
                synth.generate_response_audio('Modo no disponible')

            elif mode == configuration_json['execution_mode'][4]:
                synth.generate_response_audio('Modo no disponible')
            else:
                synth.generate_response_audio('No entendí, intenta denuveo')

            

if __name__ == '__main__':
    main()
