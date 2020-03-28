from gtts import gTTS
import os
from playsound import playsound
import numpy as np

def tts(string):
    audio = gTTS(string,slow=False ,lang='en-us',tld='co.in')
    file = './Data/audio.mp3'
    audio.save(file)
    playsound(file,True)
tts("i didn't understand that")
