from gtts import gTTS
import os
from playsound import playsound
import numpy as np

def tts(string):
    audio = gTTS(string,slow=False ,lang='en-us')
    file = './temp/tempTTS'+str(np.random.random(size=1))+".mp3"
    audio.save(file)
    playsound(file,True)
    os.remove(file)