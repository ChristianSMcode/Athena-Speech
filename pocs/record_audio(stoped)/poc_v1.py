import sounddevice as sd
import soundfile as sf
import numpy as np

fs = 44100  
seconds = 5  

myrecording = sd.rec(int(fs * seconds), samplerate=fs, channels=1)
sd.wait()  
sf.write("recording.wav", myrecording, fs)