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
        random_number_initialization=random.randint(0,2)
        random_number_prompt=random.randint(0,1)
        random_number_default=random.randint(0,1)
        print('Activalo')
        if listen_activate(configuration_json['activation_word'],LANGUAGE):
            
            synth.generate_response_audio(configuration_json['prompts']['initialization'][random_number_initialization])
            mode=recognize_option(configuration_json['execution_mode'],LANGUAGE)
        
            if mode == configuration_json['execution_mode'][0]:
                synth.generate_response_audio(configuration_json["prompts"]["mode_prompts"][random_number_prompt] + mode)

            elif mode == configuration_json['execution_mode'][1]:
                synth.generate_response_audio(configuration_json["prompts"]["mode_prompts"][random_number_prompt] + mode)

            elif mode == configuration_json['execution_mode'][2]:
                synth.generate_response_audio(configuration_json["prompts"]["mode_prompts"][random_number_prompt] + mode)

            elif mode == configuration_json['execution_mode'][3]:
                synth.generate_response_audio(configuration_json["prompts"]["mode_prompts"][random_number_prompt] + mode)

            elif mode == configuration_json['execution_mode'][4]:
                synth.generate_response_audio(configuration_json["prompts"]["mode_prompts"][random_number_prompt] + mode)
            else:
                synth.generate_response_audio(configuration_json["default_words"]["mode_not_found"][random_number_default])

            

if __name__ == '__main__':
    main()
