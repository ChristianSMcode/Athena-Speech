import sounddevice as sd
import soundfile as sf
import numpy as np
import speech_recognition as sr


def record_audio_file(sec_duration,channels_ammount=1,sample_rate_conf=44100):
    fs = sample_rate_conf  
    seconds = sec_duration  
    myrecording = sd.rec(int(fs * seconds), samplerate=fs, channels=channels_ammount)
    sd.wait()
    #sf.write('tmp/test.wav', myrecording, fs)
    return {"audio":myrecording,"fs":fs,"channels":channels_ammount}

def recognize_text_in_audio(audio_data_config):
    r = sr.Recognizer()
    audio = sr.AudioData(audio_data_config['audio'],audio_data_config['fs'], audio_data_config['channels'])
    text = r.recognize_google(audio)

